#!/usr/bin/env python
# coding: utf-8

#imports

#Topic class
class Topic:
	
	#variables
	def __init__(self):
		self.name = ""
		self.popularity = 0
		self.is_trending = False
		self.MA_time_diff = 0
	
	#setter methods
	def set_name(name):
		self.name = name

	def set_popularity(popularity):
		self.popularity = popularity

	def set_is_trending(is_trending):
		self.is_trending = is_trending
	
	#getter methods
	def get_name():
		return self.name

	def get_popularity():
		return self.popularity

	def get_is_trending():
		return self.is_trending

	def get_MA_time_diff():
		return self.MA_time_diff

	#general methods
	def increment_popularity():
		self.popularity += 1

	def update_MA_time_diff():
		#implement later
		pass

	def to_string():
		return get_name()

