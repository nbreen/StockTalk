# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
import re
import random
import datetime
import pandas as pd
import numpy as np

#connect to database
db_engine = 'django.db.backends.mysql'
db_name = 'StockTalk'
db_user = 'admin'
db_password = '13Team13'
db_host = 'cs307team13.cwbgzf4cyva5.us-east-2.rds.amazonaws.com'
db_port = '3306'

connection = pymysql.connect(db_host, db_user, db_password, db_name)
cur = connection.cursor()



def populate_recommendTopics_currentData():
	#get all usernames
	cur.execute("SELECT Username FROM UserApp_users")
	result = cur.fetchall()
	usernames = []
	for i in range(len(result)):
		usernames.append(result[i][0])

	#get trending topics
	cur.execute("SELECT TopicName from TopicApp_topic WHERE isTrending = 1 ORDER BY TrendingScore DESC")
	result = cur.fetchall()
	trending_topics = []
	for i in range(len(result)):
		trending_topics.append(result[i][0])

	#get most followed topics
	cur.execute("SELECT TopicName from TopicApp_topic ORDER BY NumberOfPosts DESC LIMIT 10")
	result = cur.fetchall()
	popular_topics = []
	for i in range(len(result)):
		popular_topics.append(result[i][0])

	for user in usernames:
		#get topics that user posted about 
		cur.execute("SELECT TopicName from PostsApp_posts WHERE Username = %s ORDER BY PostDate DESC", user)
		result = cur.fetchall()
		posted_topics = []
		for i in range(len(result)):
			posted_topics.append(result[i][0])

		#get topics that user follows
		cur.execute("SELECT TopicName from UserFollowsTopic WHERE Username = %s", user)
		result = cur.fetchall()
		followed_topics = []
		for i in range(len(result)):
			followed_topics.append(result[i][0])

		all_potential_topics = []
		posted_bias = 1.3
		trending_bias = 1.2
		popular_bias = 1.1

		#make list of posted topics not followed
		posted_not_followed_topics = []
		scores = []
		rank = 1
		#print("posted***********")
		for topic in posted_topics:
			if topic not in followed_topics and topic not in all_potential_topics:
				posted_not_followed_topics.append(topic)
				score = float(1/rank) * posted_bias
				all_potential_topics.append(topic)
				scores.append(score)
				rank += 1
				#print(topic)

		#make list of trending topics not followed
		trending_not_followed_topics = []
		rank = 1
		#print("trend***********")
		for topic in trending_topics:
			if topic not in followed_topics and topic not in all_potential_topics:
				trending_not_followed_topics.append(topic)
				score = float(1/rank) * trending_bias
				all_potential_topics.append(topic)
				scores.append(score)
				rank += 1
				#print(topic)

		#make list of popular topics not followed 
		popular_not_followed_topics = []
		rank = 1
		#print("pop***********")
		for topic in popular_topics:
			if topic not in followed_topics and topic not in all_potential_topics:
				popular_not_followed_topics.append(topic)
				score = float(1/rank) * popular_bias
				all_potential_topics.append(topic)
				scores.append(score)
				rank += 1
				#print(topic)

		#sorted(all_potential_topics,key=lambda x: 
		#for i in all_potential_topics:
			#print(i)
		#print(user)

		
		for i in range(len(all_potential_topics)):
			cur.execute("INSERT IGNORE INTO RecommendTopics(CurrentUser, RecommendedTopic, Score) VALUES (%s, %s, %s)", (user, all_potential_topics[i], scores[i]))
			connection.commit()
			#print(user)
			#print(all_potential_topics[i])
			#print(scores[i])
		
	
def update(user, topic, method):
	#new post about topic
	if method == 0:
		pass
	#followed topic
	elif method == 1:
		pass
	#unfollowed_topic
	elif method == 2:
		pass



#0 = new post, 1 = follow, 2 = unfollow
method = 0
user = '908fes'
topic = 'TSLA'
update(user, topic, method)
populate_recommendTopics_currentData()

