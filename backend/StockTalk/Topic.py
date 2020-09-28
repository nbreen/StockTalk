#!/usr/bin/env python
# coding: utf-8

#imports
import User
import Comment
import Interaction
import Timeline
import Post

#Topic class
class Topic:
	
	#variables
	def __init__(self):
		self.name = ""
		self.popularity = 0
		self.is_trending = False
		self.MA_time_diff = 0
	
	#setter methods
	def set_name(self, name):
		self.name = name

	def set_popularity(self, popularity):
		self.popularity = popularity

	def set_is_trending(self, is_trending):
		self.is_trending = is_trending
	
	#getter methods
	def get_name(self):
		return self.name

	def get_popularity(self):
		return self.popularity

	def get_is_trending(self):
		return self.is_trending

	def get_MA_time_diff(self):
		return self.MA_time_diff

	#general methods
	def increment_popularity(self):
		self.popularity += 1

	def update_MA_time_diff(self):
		#implement later
		pass

	def to_string(self):
		return get_name()

