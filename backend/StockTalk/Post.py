#!/usr/bin/env python
# coding: utf-8

#imports
#install PIL using "pip install Pillow" in cmd
from PIL import Image
from datetime import datetime
import User
import Comment
import Interaction
import Timeline
import Topic

#Post class
class Post:

	#variables
	def __init__(self):
		self.is_image = False
		self.post_text = ""
		self.post_image = Image.open("img/default_profile_pic.jpg")
		self.author = User.User()
		self.likes = 0
		self.dislikes = 0
		self.topic = Topic.Topic()
		self.comments = []
		self.users_liked = []
		self.users_disliked = []

		#set time
		current_time = datetime.now()
		self.time = current_time.strftime("%d/%m/%Y %H:%M:%S")

		#set id
		self.post_id = id(self)
	
	#setter methods
	def set_is_image(self):
		self.is_image = True

	def set_post_text(self, post_text):
		self.post_text = post_text

	def set_post_image(self, post_image):
		self.post_image = post_image	

	def set_author(self, author):
		self.author = author	

	def set_topic(self, topic):
		self.topic = topic	

	#getter methods
	def get_text(self):
		return self.post_text

	def get_image(self):
		return self.post_image

	def get_author(self):
		return self.author

	def get_likes(self):
		return self.likes

	def get_dislikes(self):
		return self.dislikes

	def get_topic(self):
		return self.topic

	def get_comments(self):
		return self.comments

	def get_id(self):
		return self.post_id

	def get_time(self):
		return self.time

	def get_users_liked(self):
		return self.get_users_liked

	def get_users_disliked(self):
		return self.get_users_disliked

	#general methods
	def increment_likes(self):
		self.likes += 1

	def decrement_likes(self):
		self.likes -= 1

	def increment_dislikes(self):
		self.dislikes += 1

	def decrement_dislikes(self):
		self.likes -= 1

	def add_comment(self, comment):
		self.comments.append(comment)

	def remove_comment(self, comment):
		self.comments.remove(comment)

	def add_user_liked(self, user):
		self.users_liked.append(user)

	def remove_user_liked(self, user):
		self.users_liked.remove(user)

	def add_user_disliked(self, user):
		self.users_disliked.append(user)

	def remove_user_disliked(self, user):
		self.users_disliked.remove(user)

	def to_string(self):
		return ("a post made by " + self.author.to_string())

