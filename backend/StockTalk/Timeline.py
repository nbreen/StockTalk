#!/usr/bin/env python
# coding: utf-8

#imports
from .user import User
from .topic import Topic
from .post import Post
from .comment import Comment

#Timeline class
class Timeline:
	
	#variables
	def __init__(self):
		self.is_user_timeline = False
		self.is_user_interaction_timeline = False
		self.is_topic_timeline = False
		self.user = None
		self.topic = None
		self.timeline = []
	
	#setter methods
	def set_is_user_timeline():
		self.is_user_timeline = True
		self.is_user_interaction_timeline = False
		self.is_topic_timeline = False

	def set_is_user_interaction_timeline():
		self.is_user_timeline = False
		self.is_user_interaction_timeline = True
		self.is_topic_timeline = False

	def set_is_topic_timeline():
		self.is_user_timeline = False
		self.is_user_interaction_timeline = False
		self.is_topic_timeline = True

	def set_user(user):
		self.user = user

	def set_topic(topic)
		self.topic = topic
	
	#getter methods
	def get_is_user_timeline()
		return self.is_user_timeline

	def get_is_user_interaction_timeline()
		return self.is_user_interaction_timeline

	def get_is_topic_timeline()
		return self.is_topic_timeline

	def get_timelime()
		return self.timeline

	#general methods
	def make_timeline():
		#implement later
		pass

	def remove_from_timeline(post):
		self.timeline.remove(post)

	def add_to_timeline(post):
		self.timeline.append(post)

