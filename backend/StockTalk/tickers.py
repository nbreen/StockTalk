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
INSERT IGNORE INTO TopicApp_topic (TopicName, IsStock) VALUES (%s, 1)
"""
for i in range(len(stock_tickers)):
	cur.execute(query, stock_tickers[i])
	connection.commit()
