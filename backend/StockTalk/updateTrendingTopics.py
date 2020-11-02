#!/usr/bin/env python
# coding: utf-8

#imports
import pymysql
import re
import random


#Time in the form of ms since 1970 with the first 5 digits removed
def update(topic, time):
	#connect to database
	db_engine = 'django.db.backends.mysql'
	db_name = 'StockTalk'
	db_user = 'admin'
	db_password = '13Team13'
	db_host = 'cs307team13.cwbgzf4cyva5.us-east-2.rds.amazonaws.com'
	db_port = '3306'
	connection = pymysql.connect(db_host, db_user, db_password, db_name)
	cur = connection.cursor()

	#how many posts to track back
	n = 3
	'''
	cur.execute("UPDATE TopicApp_topic SET CurrentMA = 0 WHERE IsStock = 1")
	connection.commit()
	'''


	#get variables from database
	cur.execute("SELECT NumberOfPosts FROM TopicApp_topic WHERE TopicName = %s", topic)
	n_posts = int(cur.fetchone()[0])

	cur.execute("SELECT PreviousMA FROM TopicApp_topic WHERE TopicName = %s", topic)
	previous_MA = int(float(cur.fetchone()[0]))

	cur.execute("SELECT CurrentMA FROM TopicApp_topic WHERE TopicName = %s", topic)
	current_MA = int(float(cur.fetchone()[0]))

	cur.execute("SELECT TimeOfLastPost FROM TopicApp_topic WHERE TopicName = %s", topic)
	last_post_time = int(cur.fetchone()[0])

	time = int(time)


	#formula for Moving average
	current_MA = int((current_MA*(n-1) + (time - last_post_time)) / n)

	#update database with this value
	cur.execute("UPDATE TopicApp_topic SET CurrentMA = %s WHERE TopicName = %s", (current_MA, topic))
	connection.commit()

	#for every n, we update the previous MA to compare the new one to
	if n_posts % n == 0:
		cur.execute("UPDATE TopicApp_topic SET PreviousMA = %s WHERE TopicName = %s", (current_MA, topic))
		connection.commit()

	if previous_MA != 0 and n_posts >= n:
		gain = current_MA / previous_MA
	else:
		gain = .01 * (n_posts + 1)

	#update database with new values
	cur.execute("UPDATE TopicApp_topic SET NumberOFPosts = %s WHERE TopicName = %s", (str(n_posts+1), topic))
	connection.commit()

	cur.execute("UPDATE TopicApp_topic SET TimeOfLastPost = %s WHERE TopicName = %s", (time, topic))
	connection.commit()

	cur.execute("UPDATE TopicApp_topic SET TrendingScore = %s WHERE TopicName = %s", (str(gain), topic))
	connection.commit()


	#update isTrending
	cur.execute("UPDATE TopicApp_topic SET isTrending = 0 WHERE isStock = 1")
	connection.commit()

	cur.execute("UPDATE TopicApp_topic AS x INNER JOIN (SELECT TopicName FROM TopicApp_topic ORDER BY TrendingScore DESC LIMIT 10) AS y SET  isTrending = 1 WHERE x.TopicName = y.TopicName")
	connection.commit()


#test function
#update("AACG","46037001")
