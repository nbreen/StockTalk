# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
import re
import names
import random
import updateTrendingTopics as utt

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

#open the raw twitter data file (many more yet to be processed)
f = open("sample_twitter_data.json", "r")

#variables needed
all_tweets = []
all_users = []
all_timestamps = []
valid_data = []

#for each line in raw twitter data
for line in f:
	pattern = '#'
	hashtag = re.search(pattern,line)

	#if the post has a hashtag
	if hashtag != None:

		#regex for text
		pattern = '"text":".+?"'
		text = re.findall(pattern, line)

		#regex for user
		pattern = '"screen_name":".+?"'
		user = re.findall(pattern, line)

		#regex for timestamp
		pattern = '"timestamp_ms":".+?"'
		timestamp = re.findall(pattern, line)

		#get usernames
		for u in user:
			u = re.sub(r'screen_name":"',"",u)
			u = re.sub(r'"',"",u)
			all_users.append(u)

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
					valid_data.append((t, all_users[len(all_users)-1], all_timestamps[len(all_timestamps)-1]))

#remove duplicate users
all_users = list(dict.fromkeys(all_users))



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
	print("Post: " + str(data[0][0]))
	print("User: " + str(data[0][1]))
	print("Timestamp(ms): " + str(data[0][2]))
	print("")


cur.execute("SELECT MAX(UserID) FROM UserApp_users")
max_id = cur.fetchone()
next_id = max_id[0]

cur.execute("SELECT MAX(PostId) FROM PostApp_posts")
max_post_id = cur.fetchone()
next_post_id = max_post_id[0]

#create users in database with a post
for i in range(len(data_with_ticker)):
#for i in range(1):
	next_id += 1
	username = data_with_ticker[i][0][1]
	full_name = names.get_full_name()
	email = str(data_with_ticker[i][0][1]) + "@email.com"
	password = "password"
	age = 18
	younger_bias = random.randrange(0,5)
	if younger_bias < 3:
		age = random.randrange(18,35)
	else:
		age = random.randrange(18,70)

	bio = "My name is " + str(full_name) + ". I am " + str(age) + " years old and love to talk about stocks!"

	profile_image = "None"
	followers = 0
	following = 0
	n_posts = 0
	
	cur.execute("INSERT IGNORE INTO UserApp_users(UserID, Username, Fullname, Email, Password, UserAge, Bio, ProfileImage, Followers, Following, NumberOfPosts) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 0, 0, 0)", (str(next_id), username, full_name, email, password, str(age), bio, str(profile_image)))
	connection.commit()

	next_post_id += 1
	topic = data_with_ticker[i][1]
	post_type = 0
	post = data_with_ticker[i][0][0]
	#remove first 5 digits (15830) for correct int size
	date = data_with_ticker[i][0][2][4:]
	anon = 0

	cur.execute("SELECT UserID FROM UserApp_users WHERE Username = %s", str(username))
	user_id_for_post = cur.fetchone()[0]

	cur.execute("INSERT INTO PostApp_posts(PostId, UserID, TopicName, PostType, Post, PostDate, Anonymous) VALUES (%s, %s, %s, 0, %s, %s, 0)", (str(next_post_id), str(user_id_for_post), str(topic), str(post), str(date)))
	connection.commit()

	cur.execute("SELECT NumberOfPosts FROM UserApp_users WHERE Username = %s", username)
	n_posts = str(cur.fetchone()[0]) + str(1)
	
	cur.execute("UPDATE UserApp_users SET NumberOfPosts = %s WHERE Username = %s", (n_posts, username))
	connection.commit()

	utt.update(str(topic), str(date))

