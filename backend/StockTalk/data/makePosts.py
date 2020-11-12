# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
import re
import names
import random
import updateTrendingTopics as utt
import datetime

#connect to database
db_engine = 'django.db.backends.mysql'
db_name = 'StockTalk'
db_user = 'admin'
db_password = '13Team13'
db_host = 'cs307team13.cwbgzf4cyva5.us-east-2.rds.amazonaws.com'
db_port = '3306'

connection = pymysql.connect(db_host, db_user, db_password, db_name)

cur = connection.cursor()

#get all valid topics in database
cur.execute("SELECT TopicName FROM TopicApp_topic ")
topics = cur.fetchall()

'''
cur.execute("UPDATE TopicApp_topic SET isTrending = 0")
connection.commit()
'''

#open the raw twitter data file (many more yet to be processed)
f = open("sample_twitter_data.json", "r")

#variables needed
all_tweets = []
all_timestamps = []
valid_data = []

cur.execute("SELECT Username FROM UserApp_users")
result = cur.fetchall()
all_users = []
for i in range(len(result)):
	all_users.append(result[i][0])


#for each line in raw twitter data
for line in f:
	pattern = '#'
	hashtag = re.search(pattern,line)

	#if the post has a hashtag
	if hashtag != None:

		#regex for text
		pattern = '"text":".+?"'
		text = re.findall(pattern, line)

		#regex for timestamp
		pattern = '"timestamp_ms":".+?"'
		timestamp = re.findall(pattern, line)

		#get timestamps
		for ts in timestamp:
			ts = re.sub(r'timestamp_ms":"',"",ts)
			ts = re.sub(r'"',"",ts)
			all_timestamps.append(ts)

		#get texts
		for t in text:
			t = re.sub(r'text":"',"",t)
			t = re.sub(r'"',"",t)
			t = re.sub(r'\\u[a-zA-Z0-9]{4}',"",t)
			t = re.sub(r'\\[a-zA-Z]',"",t)
			t = re.sub(r'&amp;',"&",t)
			t = re.sub(r'\\\/',"/",t)

			#filter out bad hashtag data
			if len(t) > 0:
				pattern = '#[a-z]{1,4}([\s]|$)'
				valid_hashtag = re.search(pattern,t.lower())

				if valid_hashtag != None:
					t = re.sub(r'#[a-z0-9]{5,}([\s]|$)',"",t.lower())
					all_tweets.append(t)
					valid_data.append((t, random.choice(all_users), all_timestamps[len(all_timestamps)-1]))


#for all data that contains a potential valid ticker, see if it is indeed valid
data_with_ticker = []
index = 0

for data in valid_data:
	print("Processing: " + str(index+1) + "/" + str(len(valid_data)))
	index += 1
	for topic in topics:
		pattern = '#' + topic[0].lower() + '([\s]|$)'
		ticker = re.search(pattern, data[0].lower())
		if ticker != None and data[0][0:4] != "rt @" :
			ticker = ticker.group(0)[1:].upper()
			if ticker[-1] == " ":
				ticker = ticker[:-1]
			data_with_ticker.append((data, ticker))

#print all posts with user and timestamp that involve a valid topic in our database
for data in data_with_ticker:
	print(data[1])
	data = [data[0][0], data[0][1], data[0][2]]
	
	print("Post: " + str(data[0]))
	print("User: " + str(data[1]))

	data[2] = (datetime.datetime.fromtimestamp(int(data[2])/1000.0))
	print("Timestamp: " + str(data[2]))
	print(data[1])
	print("")


cur.execute("SELECT MAX(UserID) FROM UserApp_users")
max_id = cur.fetchone()
next_id = max_id[0]

cur.execute("SELECT MAX(PostId) FROM PostsApp_posts")
max_post_id = cur.fetchone()
next_post_id = max_post_id[0]

#create users in database with a post
for i in range(len(data_with_ticker)):
#for i in range(1):
	username = data_with_ticker[i][0][1]
	ticker = data_with_ticker[i][1]
	next_post_id += 1
	topic = data_with_ticker[i][1]
	post_type = 0
	post = data_with_ticker[i][0][0]
	date = data_with_ticker[i][0][2]
	anon = 0
	downvotes = 0
	upvotes = 0
	post_image = 'None'

	cur.execute("SELECT UserID FROM UserApp_users WHERE Username = %s", str(username))
	user_id_for_post = cur.fetchone()[0]

	date_formatted = datetime.datetime.fromtimestamp(int(date)/1000)
	date_formatted = date_formatted.strftime('%Y-%m-%d %H:%M:%S')

	cur.execute("INSERT INTO PostsApp_posts(PostId, Username, TopicName,  PostType, Post, PostDate, Downvotes, Upvotes, Anonymous, PostImage) VALUES (%s, %s, %s, 0, %s, %s, 0, 0, 0, 'None')", (int(next_post_id), username, str(topic), str(post), date_formatted))
	connection.commit()

	cur.execute("SELECT NumberOfPosts FROM UserApp_users WHERE Username = %s", username)
	n_posts = int(cur.fetchone()[0]) + 1
	
	cur.execute("UPDATE UserApp_users SET NumberOfPosts = %s WHERE Username = %s", (n_posts, username))
	connection.commit()

	utt.update(str(topic), date_formatted)

