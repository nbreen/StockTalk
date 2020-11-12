#imports
from get_all_tickers import get_tickers as gt
import os
import csv
import pymysql

stock_tickers = gt.get_tickers()
db_engine = 'django.db.backends.mysql'
db_name = 'StockTalk'
db_user = 'admin'
db_password = '13Team13'
db_host = 'cs307team13.cwbgzf4cyva5.us-east-2.rds.amazonaws.com'
db_port = '3306'

connection = pymysql.connect(db_host, db_user, db_password, db_name)

cur = connection.cursor()

query = """
INSERT IGNORE INTO TopicApp_topic (TopicName, IsStock, isTrending, TrendingScore, NumberOfPosts, PreviousMA, CurrentMA, TimeOfLastPost) VALUES (%s, 1, 0, 0.00, 0, 0, 0, '2020-01-01 00:00:00')
"""
for i in range(len(stock_tickers)):
	print(i)
	cur.execute(query, stock_tickers[i])
	connection.commit()
