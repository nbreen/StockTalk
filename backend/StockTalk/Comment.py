#!/usr/bin/env python
# coding: utf-8

#imports
from datetime import datetime
import User
import Interaction
import Timeline
import Topic
import Post

#Comment class
class Comment:
	
	#variables
	def __init__(self):
		self.likes = 0
		self.dislikes = 0
		self.author = User.User()
		self.post = Post.Post()
		self.text = ""
		self.users_liked = []
		self.users_disliked = []

		#set time
		current_time = datetime.now()
		self.time = current_time.strftime("%d/%m/%Y %H:%M:%S")
	
	#setter methods
	def set_author(self, author):
		self.author = author

	def set_post(self, post):
		self.post = post

	def set_text(self, text):
		self.text = text
	
	#getter methods
	def get_author(self):
		return self.author

	def get_likes(self):
		return self.likes

	def get_dislikes(self):
		return self.dislikes

	def get_post(self):
		return self.post

	def get_text(self):
		return self.text

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

	def add_user_liked(self, user):
		self.users_liked.append(user)

	def remove_user_liked(self, user):
		self.users_liked.remove(user)

	def add_user_disliked(self, user):
		self.users_disliked.append(user)

	def remove_user_disliked(self, user):
		self.users_disliked.remove(user)

	def to_string(self):
		return ("a comment made by " + self.author.to_string())

