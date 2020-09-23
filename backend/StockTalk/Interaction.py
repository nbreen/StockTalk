#!/usr/bin/env python
# coding: utf-8

#imports
from datetime import datetime
import User
import Comment
import Timeline
import Topic
import Post

#Interaction class
class Interaction:
	
	#variables
	def __init__(self):
		self.text = ""
		self.user = User.User()
		self.post_interacted_with = Post.Post()
		self.user_interacted_with = User.User()
		self.comment_interacted_with = Comment.Comment()
		self.topic_interacted_with = Topic.Topic()
		self.is_liked_interaction = False
		self.is_disliked_interaction = False
		self.is_comment_interaction = False
		self.is_follow_interaction = False
		self.is_post_interaction = False

		#set time
		current_time = datetime.now()
		self.time = current_time.strftime("%d/%m/%Y %H:%M:%S")
		
	
	#setter methods
	def set_post_interacted_with(self, post):
		self.post_interacted_with = post
		self.text = post.to_string()

	def set_user_interacted_with(self, user):
		self.user_interacted_with = user
		self.text = user.to_string()

	def set_comment_interacted_with(self, comment):
		self.comment_interacted_with = comment
		self.text = comment.to_string()

	def set_topic_interacted_with(self, topic):
		self.topic_interacted_with = topic
		self.text = topic.to_string()
	
	def set_is_liked_interaction(self):
		self.is_liked_interaction = True

	def set_is_disliked_interaction(self):
		self.is_disliked_interaction = True

	def set_is_comment_interaction(self):
		self.is_comment_interaction = True

	def set_is_follow_interaction(self):
		self.is_follow_interaction = True

	def set_is_post_interaction(self):
		self.is_post_interaction = True

	def set_text(self):
		if self.is_liked_interaction == True:
			self.text = self.user.to_string() + " liked " + self.text
		elif self.is_disliked_interaction == True:
			self.text = self.user.to_string() + " disliked " + self.text
		elif self.is_comment_interaction == True:
			self.text = self.user.to_string() + " commented on " + self.text
		elif self.is_follow_interaction == True:
			self.text = self.user.to_string() + " followed " + self.text
		elif self.is_post_interaction == True:
			self.text = self.user.to_string() + " posted a new post"
		else:
			raise ValueError("Interaction type not set.")

	def set_user(self, user):
		self.user = user
				
	#getter methods
	def get_is_liked_interaction(self):
		return self.is_liked_interaction

	def get_is_disliked_interaction(self):
		return self.is_disliked_interaction

	def get_is_comment_interaction(self):
		return self.is_comment_interaction

	def get_is_follow_interaction(self):
		return self.is_follow_interaction

	def get_is_post_interaction(self):
		return self.is_post_interaction

	def get_post_interacted_with():
		return self.post_interacted_with

	def get_user_interacted_with():
		return self.user_interacted_with

	def get_comment_interacted_with():
		return self.comment_interacted_with

	def get_topic_interacted_with():
		return self.topic_interacted_with

	def get_time(self):
		return self.time

	def get_text(self):
		return self.text

	def get_user(self):
		return self.user

	def to_string(self):
		return self.text

