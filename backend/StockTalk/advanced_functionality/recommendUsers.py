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

def recommendUsers():
	#get all usernames
	cur.execute("SELECT Username FROM UserApp_users")
	result = cur.fetchall()
	usernames = []
	for i in range(len(result)):
		usernames.append(result[i][0])

	#get all topics
	cur.execute("SELECT TopicName from TopicApp_topic")
	result = cur.fetchall()
	topics = []
	for i in range(len(result)):
		topics.append(result[i][0])

	#create empty dataframe
	data = {}
	data['Username'] = usernames
	for topic in topics:
		array = []
		for user in usernames:
			array.append(0)
		data[topic] = array
	columns = topics.insert(0, 'Username')
	df = pd.DataFrame(data, columns = topics)
	#print(df)

	#add data to dataframe
	for index, row in df.iterrows():
		user = row['Username']
		#get topics followed
		cur.execute("SELECT TopicName from UserFollowsTopic WHERE Username = %s", user)
		result = cur.fetchall()
		followed_topics = []
		for i in range(len(result)):
			followed_topics.append(result[i][0])

		for topic in followed_topics:
			row[topic] = 1

	#remove user column
	user_column = df['Username']
	del df['Username']

	pca = PCA()
	df_pca = pca.fit_transform(df)
	df_pca = pd.DataFrame(df_pca)
	print(df_pca)

	
	'''
	print(df)
	#find k using elbow method
	k_rng = range(1,10)
	sse = []
	for k in k_rng:
		km = KMeans(n_clusters=k)
		km.fit(df)
		sse.append(km.inertia_)

	#plot sse
	fig = plt.figure()
	plt.xlabel('K')
	plt.ylabel('Sum of squared error')
	plt.plot(k_rng, sse)
	fig.savefig('sse_recommendusers.png')
	'''
#knn_cluster()
recommendUsers()

