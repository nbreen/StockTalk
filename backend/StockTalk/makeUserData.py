# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
import re

#conncet to database
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
	print("Processing: " + str(index) + "/" + str(len(valid_data)))
	index += 1
	for topic in topics:
		pattern = '#' + topic[0].lower() + '([\s]|$)'
		search = re.search(pattern, data[0].lower())
		if search != None:
			data_with_ticker.append(data)

#print all posts with user and timestamp that involve a valid topic in our database
for data in data_with_ticker:
	print("Post: " + str(data[0]))
	print("User: " + str(data[1]))
	print("Timestamp(ms): " + str(data[2]))
	print("")




