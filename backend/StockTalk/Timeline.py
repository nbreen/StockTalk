#!/usr/bin/env python
# coding: utf-8

#imports
import User
import Comment
import Interaction
import Topic
import Post

#Timeline class
class Timeline:
	
	#variables
	def __init__(self):
		self.is_user_timeline = False
		self.is_user_interaction_timeline = False
		self.is_topic_timeline = False
		self.user = User.User()
		self.topic = Topic.Topic()
		self.timeline = []
	
	#setter methods
	def set_is_user_timeline(self):
		self.is_user_timeline = True
		self.is_user_interaction_timeline = False
		self.is_topic_timeline = False

	def set_is_user_interaction_timeline(self):
		self.is_user_timeline = False
		self.is_user_interaction_timeline = True
		self.is_topic_timeline = False

	def set_is_topic_timeline(self):
		self.is_user_timeline = False
		self.is_user_interaction_timeline = False
		self.is_topic_timeline = True

	def set_user(self, user):
		self.user = user

	def set_topic(self, topic):
		self.topic = topic
	
	#getter methods
	def get_is_user_timeline(self):
		return self.is_user_timeline

	def get_is_user_interaction_timeline(self):
		return self.is_user_interaction_timeline

	def get_is_topic_timeline(self):
		return self.is_topic_timeline

	def get_timelime(self):
		return self.timeline

	#general methods
	def make_timeline(self):
		#implement later
		pass

	def remove_from_timeline(self, post):
		self.timeline.remove(post)

	def add_to_timeline(self, post):
		self.timeline.append(post)

