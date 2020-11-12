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

#get all users
cur.execute("SELECT Username FROM UserApp_users")
result = cur.fetchall()
all_users = []
for i in range(len(result)):
	all_users.append(result[i][0])


#get random time
cur.execute("SELECT PostDate FROM PostsApp_posts")
result = cur.fetchall()
random_dates = []
for i in range(len(result)):
	random_dates.append(result[i][0])
data_with_ticker = []

random_users = []
for i in range(100):
	random_users.append(random.choice(all_users))

for user in random_users:
	#get random number of posts for followed topic
	low_n_bias = random.randint(0,4)
	if low_n_bias == 2:
		#get followed topics
		cur.execute("SELECT TopicName FROM UserFollowsTopic WHERE Username = %s", user)
		result = cur.fetchall()
		followed_topics = []
		for i in range(len(result)):
			followed_topics.append(result[i][0])

		for topic in followed_topics:
			random_n = random.randint(0,7)
			data_with_ticker.append((('#' + str(topic),user,random.choice(random_dates)), topic))
			

#print all posts with user and timestamp that involve a valid topic in our database
print(data_with_ticker)
for data in data_with_ticker:
	print(data[1])
	data = [data[0][0], data[0][1], data[0][2]]
	
	print("Post: " + str(data[0]))
	print("User: " + str(data[1]))

	print("Timestamp: " + str(data[2]))
	print(data[1])
	print("")


cur.execute("SELECT MAX(PostId) FROM PostsApp_posts")
max_post_id = cur.fetchone()
next_post_id = max_post_id[0]

#posts
for i in range(len(data_with_ticker)):
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

	cur.execute("INSERT INTO PostsApp_posts(PostId, Username, TopicName,  PostType, Post, PostDate, Downvotes, Upvotes, Anonymous, PostImage) VALUES (%s, %s, %s, 0, %s, %s, 0, 0, 0, 'None')", (int(next_post_id), username, str(topic), str(post), date))
	connection.commit()

	cur.execute("SELECT NumberOfPosts FROM UserApp_users WHERE Username = %s", username)
	n_posts = int(cur.fetchone()[0]) + 1
	
	cur.execute("UPDATE UserApp_users SET NumberOfPosts = %s WHERE Username = %s", (n_posts, username))
	connection.commit()
	print(date)
	utt.update(str(topic), date)
	
