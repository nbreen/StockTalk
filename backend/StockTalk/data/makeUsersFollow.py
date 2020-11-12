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
cur.execute("SELECT MAX(UserID) FROM UserApp_users")
n_users = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM TopicApp_topic")
n_topics = cur.fetchone()[0]

for i in range(n_users):
	print(str(i) + "/" + str(n_users))
	follow_n_users = random.randrange(1,10)
	follow_n_topics = random.randrange(1,5)

	cur.execute("SELECT Username FROM UserApp_users WHERE UserID = %s", i)
	user_a = cur.fetchone()
	if user_a != None:
		user_a = user_a[0]
		for j in range(follow_n_users):
			cur.execute("SELECT Username FROM UserApp_users ORDER BY RAND() LIMIT 1")
			user_b = cur.fetchone()[0]

			cur.execute("INSERT IGNORE INTO UserFollowsUser(DoingFollowing, BeingFollowed) VALUES (%s, %s)", (user_a, user_b))
			connection.commit()

			#following
			cur.execute("SELECT Following FROM UserApp_users WHERE Username = %s", user_a)
			n_following = cur.fetchone()[0]

			#followers
			cur.execute("SELECT Followers FROM UserApp_users WHERE Username = %s", user_b)
			n_followers = cur.fetchone()[0]

			cur.execute("INSERT IGNORE INTO UserFollowsUser(DoingFollowing, BeingFollowed) VALUES (%s, %s)", (user_a, user_b))
			connection.commit()

			cur.execute("UPDATE UserApp_users SET Following = %s WHERE Username = %s", (n_following+1, user_a))
			connection.commit()

			cur.execute("UPDATE UserApp_users SET Followers = %s WHERE Username = %s", (n_followers+1, user_b))
			connection.commit()
		

		for j in range(follow_n_topics):
			cur.execute("SELECT TopicName FROM TopicApp_topic ORDER BY RAND() LIMIT 1")
			topic_a = cur.fetchone()[0]

			cur.execute("INSERT IGNORE INTO UserFollowsTopic(Username, TopicName) VALUES (%s, %s)", (user_a, topic_a))
			connection.commit()
		
