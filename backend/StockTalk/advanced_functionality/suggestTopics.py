# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
import re
import random
import datetime
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
import pandas as pd

#connect to database
db_engine = 'django.db.backends.mysql'
db_name = 'StockTalk'
db_user = 'admin'
db_password = '13Team13'
db_host = 'cs307team13.cwbgzf4cyva5.us-east-2.rds.amazonaws.com'
db_port = '3306'

connection = pymysql.connect(db_host, db_user, db_password, db_name)

cur = connection.cursor()


def knn_cluster():
	#get all usernames
	cur.execute("SELECT Username FROM UserApp_users")
	result = cur.fetchall()
	usernames = []
	for i in range(len(result)):
		usernames.append(result[i][0])

	#get current trending topics
	cur.execute("SELECT TopicName FROM TopicApp_topic WHERE isTrending = 1 ORDER BY TrendingScore DESC")
	result = cur.fetchall()
	trending_topics = []
	for i in range(len(result)):
		trending_topics.append(result[i][0])



	values_list = []
	n_trending_topic_posts_list = []
	n_followed_topic_posts_list = []
	#cluster each user
	for username in usernames:
		#get recent topics used by user
		cur.execute("SELECT TopicName FROM PostsApp_posts WHERE Username = %s ORDER BY PostDate Desc", username)
		result = cur.fetchall()
		recent_topics = []
		for i in range(len(result)):
			recent_topics.append(result[i][0])

		#get topics the user follows
		cur.execute("SELECT * FROM UserFollowsTopic WHERE Username = %s", username)
		result = cur.fetchall()
		followed_topics = []
		for i in range(len(result)):
			followed_topics.append(result[i][1])

		#get number of posts that use a trending topic
		n_trending_topic_posts = 0

		for topic in recent_topics:
			if topic in trending_topics:
				n_trending_topic_posts += 1

		#get number of posts about a followed topic
		n_followed_topic_posts = 0

		for topic in recent_topics:
			if topic in followed_topics:
				n_followed_topic_posts += 1

		values_list.append((n_trending_topic_posts,n_followed_topic_posts))
		n_trending_topic_posts_list.append(n_trending_topic_posts)
		n_followed_topic_posts_list.append(n_followed_topic_posts)

	#plot inital scatter plot
	fig = plt.figure()
	plt.plot(n_trending_topic_posts_list,n_followed_topic_posts_list, 'ro')
	fig.savefig('scatterplot.png')

	#create dataframe with features
	df = pd.DataFrame(list(zip(n_trending_topic_posts_list, n_followed_topic_posts_list)), columns =["trending_topics", "followed_topics"])

	#scale features
	max_trending = df['trending_topics'].max()
	max_followed = df['followed_topics'].max()
	
	for index, row in df.iterrows():
		df.at[index, "trending_topics"] = row[0]*max_followed
		df.at[index, "followed_topics"] = row[1]* max_trending
	
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
	fig.savefig('sse.png')
	
	#perform k means with correct k value
	km = KMeans(n_clusters=3)
	y_predicted = km.fit_predict(df)

	#create clusters
	df['cluster'] = y_predicted
	df1 = df[df.cluster==0]
	df2 = df[df.cluster==1]
	df3 = df[df.cluster==2]
	fig = plt.figure()

	#plot clusters
	plt.scatter(df1['trending_topics'], df1['followed_topics'], color = 'green')
	plt.scatter(df2['trending_topics'], df2['followed_topics'], color = 'red')
	plt.scatter(df3['trending_topics'], df3['followed_topics'], color = 'blue')

	plt.xlabel("trending topics")
	plt.ylabel("followed topics")
	plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1], color = 'black', marker='*', label='centroid')

	fig.savefig('clusters.png')	

	#print(y_predicted)

	for i in range(len(usernames)):
		cur.execute("UPDATE UserApp_users SET Cluster = %s WHERE Username = %s", (int(y_predicted[i]), str(usernames[i])))
		connection.commit()

def updateProfiles():
	pass
	'''
	#get all usernames
	cur.execute("SELECT Username FROM UserApp_users")
	result = cur.fetchall()
	usernames = []
	for i in range(len(result)):
		usernames.append(result[i][0])	

	#get all bios
	cur.execute("SELECT Bio FROM UserApp_users")
	result = cur.fetchall()
	bios = []
	for i in range(len(result)):
		bios.append(result[i][0])	

	#get all users with profile
	cur.execute("SELECT Username FROM ProfileApp_profiles")
	result = cur.fetchall()
	profiles = []
	for i in range(len(result)):
		profiles.append(result[i][0])	


	for i in range(len(usernames)):
		if usernames[i] not in profiles:
			image = 'default.png'
			cur.execute("INSERT IGNORE INTO ProfileApp_profiles(Username, Bio, ProfileImage) VALUES (%s, %s, %s)", (usernames[i], bios[i], image))
			connection.commit()

	'''
	'''
	#get all usernames
	cur.execute("SELECT Username FROM UserApp_users")
	result = cur.fetchall()
	usernames = []
	for i in range(len(result)):
		usernames.append(result[i][0])	

	#get all bios
	cur.execute("SELECT Bio FROM UserApp_users")
	result = cur.fetchall()
	bios = []
	for i in range(len(result)):
		bios.append(result[i][0])

	for i in range(len(bios)):
		if bios[i] == None:
			cur.execute("UPDATE ProfileApp_profiles SET Bio = 'my bio' WHERE Username = %s", (usernames[i]))
			connection.commit()	
	'''	

def getTrendingTopics():
	cur.execute("SELECT TopicName FROM TopicApp_topic WHERE isTrending = 1 ORDER BY TrendingScore DESC")
	result = cur.fetchall()
	trending_topics = []
	for i in range(len(result)):
		trending_topics.append(result[i][0])

	return trending_topics	

def getFollowedTopics(user):
	#get topics the user follows
	cur.execute("SELECT * FROM UserFollowsTopic WHERE Username = %s", user)
	result = cur.fetchall()
	followed_topics = []
	for i in range(len(result)):
		followed_topics.append(result[i][1])

	return followed_topics

def getAllTopics():
	#get topics the user follows
	cur.execute("SELECT TopicName FROM TopicApp_topic")
	result = cur.fetchall()
	all_topics = []
	for i in range(len(result)):
		all_topics.append(result[i][0])

	return all_topics


#needs to be called on every keystroke
def update(user, post_text):
	#get cluster for user
	cur.execute("SELECT Cluster FROM UserApp_users WHERE Username = %s", str(user))
	cluster = cur.fetchone()[0]
	suggested_topics = []
	trending_topics = getTrendingTopics()	
	followed_topics = getFollowedTopics(user)
	all_topics = getAllTopics()

	#search for # symbol
	pattern = '\*[a-zA-Z]+'
	hashtag = re.search(pattern, post_text)

	#default suggestion depends on knn cluster result
	if hashtag == None:
		#if cluster is 0, user posts about trending topics often
		if cluster == 0:
			return trending_topics

		#if cluster is 1, user posts about trending topics and followed topics evenly
		if cluster == 1:
			for topic in trending_topics:
				suggested_topics.append(topic)
			for topic in followed_topics:
				suggested_topics.append(topic)

			suggest_ten_topics = []
			for i in range(10):
				random.sample(suggested_topics, k=10)
			suggested_topics = suggest_ten_topics

		#if cluster is 2, user posts about followed topics often
		if cluster == 2:
			suggested_topics = followed_topics

	else:
		potential_topic = re.findall(pattern, post_text)[0][1:].lower()
		pattern = '^' + potential_topic
		#print(potential_topic)
		#if cluster is 0, user posts about trending topics often
		if cluster == 0:
			for topic in trending_topics:
				match = re.search(pattern, topic.lower())
				if match != None:
					suggested_topics.append(topic)

			for topic in all_topics:
				match = re.search(pattern, topic.lower())
				if match != None and topic not in suggested_topics:
					suggested_topics.append(topic)
					
		#if cluster is 1, user posts about trending topics and followed topics evenly
		if cluster == 1:

			for topic in trending_topics:
				match = re.search(pattern, topic.lower())
				if match != None:
					suggested_topics.append(topic)

			for topic in followed_topics:
				match = re.search(pattern, topic.lower())
				if match != None and topic not in suggested_topics:
					suggested_topics.append(topic)

			for topic in all_topics:
				match = re.search(pattern, topic.lower())
				if match != None and topic not in suggested_topics:
					suggested_topics.append(topic)
			
		#if cluster is 2, user posts about followed topics often
		if cluster == 2:

			for topic in followed_topics:
				match = re.search(pattern, topic.lower())
				if match != None and topic not in suggested_topics:
					suggested_topics.append(topic)

			for topic in all_topics:
				match = re.search(pattern, topic.lower())
				if match != None and topic not in suggested_topics:
					suggested_topics.append(topic)
	if len(suggested_topics) < 1:
		suggested_topics = trending_topics
	#print(suggested_topics[:10])
	return suggested_topics[:10]


user = '9O8fes'
text = 'sd *markt'
#update(user, text)
#updateProfiles()
#knn_cluster()


