# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
import re
import random
import datetime
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

def populate_recommendUsers_currentData():
	#get all usernames
	cur.execute("SELECT Username FROM UserApp_users")
	result = cur.fetchall()
	usernames = []
	for i in range(len(result)):
		usernames.append(result[i][0])

	result_list = []
	#for each user
	for user in usernames:
		#get users the user is following 
		cur.execute("SELECT BeingFollowed from UserFollowsUser WHERE DoingFollowing = %s", user)
		result = cur.fetchall()
		following = []
		for i in range(len(result)):
			following.append(result[i][0])	

		print(user)
		common_follower_list = []
		#for every other user
		for user2 in usernames:
			if user2 is not user:
				#get users the user is following 
				cur.execute("SELECT BeingFollowed from UserFollowsUser WHERE DoingFollowing = %s", user2)
				result = cur.fetchall()
				following2 = []
				for i in range(len(result)):
					following2.append(result[i][0])	

				#get number of common followers
				n_common_followers = 0
				for f in following:
					if f in following2:
						n_common_followers += 1
				
				common_follower_list.append([user2, n_common_followers])

		common_follower_list = sorted(common_follower_list, key=lambda x: x[1], reverse=True)

		i = 0
		for row in common_follower_list:
			result_list.append([user, row[0], row[1]])
			i+=1
			if i > 9:
				break
		#break

	#print(result_list)

	for row in result_list:
		cur.execute("INSERT IGNORE INTO RecommendUsers(CurrentUser, RecommendedUser, Score) VALUES (%s, %s, %s)", (row[0], row[1], row[2]))
		connection.commit()


def update(user1, user2, method):

	#get all users that follow user2
	cur.execute("SELECT DoingFollowing from UserFollowsUser WHERE BeingFollowed = %s", user2)
	result = cur.fetchall()
	common_following = []
	for i in range(len(result)):
		common_following.append(result[i][0])	

	#get all current recommendedusers for user1
	cur.execute("SELECT RecommendedUser from RecommendUsers WHERE CurrentUser = %s ORDER BY SCORE DESC", user1)
	result = cur.fetchall()
	recommended_users = []
	for i in range(len(result)):
		recommended_users.append(result[i][0])	

	#remove user2 from recommended users
	if user2 in recommended_users:
		cur.execute("DELETE FROM RecommendUsers WHERE CurrentUser = %s AND RecommendedUser = %s", (user1, user2))
		connection.commit()

	#followed user method
	#when a user1 follows user2, every user that follows user2 needs to be given +1 common follower score, and update table accordingly (Some might not be recommendedusers yet).
	if method == 0:
		#update table for each common following
		for i in range(len(common_following)):

			#get score for user in table
			cur.execute("SELECT Score from RecommendUsers WHERE CurrentUser = %s AND RecommendedUser = %s", (user1, common_following[i]))
			score_for_user = cur.fetchone()
			if score_for_user is None:
				score_for_user = 0
			else:
				score_for_user = score_for_user[0]

			#if it is in the table already, add 1
			if common_following[i] in recommended_users:
				
				score_for_user += 1

								
				cur.execute("UPDATE RecommendUsers SET Score = %s WHERE CurrentUser = %s AND RecommendedUser = %s", (score_for_user, user1, common_following[i]))
				connection.commit()

			#otherwise create a new entry				
			else:
				cur.execute("INSERT IGNORE INTO RecommendUsers(CurrentUser, RecommendedUser, Score) VALUES (%s, %s, 1)", (user1, common_following[i]))
				connection.commit()
				

	#unfollowed user method
	#when a user1 unfollows user2, every user that follows user2 needs to be given -1 common follower score, and update table accordingly (possible they aren't in recommendedusers)
	elif method == 1:

		#update table
		for i in range(len(common_following)):
			if common_following[i] in recommended_users:

				cur.execute("SELECT Score from RecommendUsers WHERE CurrentUser = %s AND RecommendedUser = %s", (user1, common_following[i]))
				score_for_user = cur.fetchone()
				if score_for_user is None:
					score_for_user = 0
				else:
					score_for_user = score_for_user[0]
				#get score and subtract 1
				if score_for_user > 0:
					score_for_user -= 1	
					
					cur.execute("UPDATE RecommendUsers SET Score = %s WHERE CurrentUser = %s AND RecommendedUser = %s", (score_for_user, user1, common_following[i]))
					connection.commit()
					
user1 = '9O8fes'
user2 = 'aommiemj'
method = 0
update(user1, user2, method)
#populate_recommendUsers_currentData()

