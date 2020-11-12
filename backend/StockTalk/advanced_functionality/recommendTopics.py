# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
import re
import random
import updateTrendingTopics as utt
import datetime
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

#connect to database
db_engine = 'django.db.backends.mysql'
db_name = 'StockTalk'
db_user = 'admin'
db_password = '13Team13'
db_host = 'cs307team13.cwbgzf4cyva5.us-east-2.rds.amazonaws.com'
db_port = '3306'

connection = pymysql.connect(db_host, db_user, db_password, db_name)
cur = connection.cursor()



def recommendTopics():
	pass

recommendTopics()

