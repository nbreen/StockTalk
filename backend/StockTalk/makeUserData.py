# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql

db_engine = 'django.db.backends.mysql'
db_name = 'StockTalk'
db_user = 'admin'
db_password = '13Team13'
db_host = 'cs307team13.cwbgzf4cyva5.us-east-2.rds.amazonaws.com'
db_port = '3306'

connection = pymysql.connect(db_host, db_user, db_password, db_name)

cur = connection.cursor()

cur.execute("SELECT * FROM UserApp_users ")
username = cur.fetchall()

for user in username:
	print(user)


