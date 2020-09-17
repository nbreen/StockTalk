#!/usr/bin/env python
# coding: utf-8

#imports
from datetime import date

#Interaction class
class Interaction:
	
	#variables
	def __init__(self):
		self.text = ""
		self.user = None
		self.object_interacted_with = None
		self.is_liked_interaction = False
		self.is_disliked_interaction = False
		self.is_comment_interaction = False
		self.is_follow_interaction = False

		#set time
		current_time = datetime.now()
		self.time = current_time.strftime("%d/%m/%Y %H:%M:%S")
		
	
	#setter methods
	def set_object_interacted_with(object_interacted_with):
		self.object.interacted_with = object_interacted_with
	
	def set_is_liked_interaction():
		self.is_liked_interaction = True

	def set_is_disliked_interaction():
		self.is_disliked_interaction = True

	def set_is_comment_interaction():
		self.is_comment_interaction = True

	def set_is_follow_interaction():
		self.is_follow_interaction = True

	def set_text():
		if self.is_liked_interaction == True:
			self.text = self.user.to_string() + " liked " + self.object_interacted_with.to_string
		else if self.is_disliked_interaction == True:
			self.text = self.user.to_string() + " disliked " + self.object_interacted_with.to_string
		else if self.is_comment_interaction == True:
			self.text = self.user.to_string() + " commented on " + self.object_interacted_with.to_string
		else if self.is_follow_interaction == True:
			self.text = self.user.to_string() + " followed " + self.object_interacted_with.to_string
		else:
			raise ValueError("Interaction type not set.")

	def set_user(user):
		self.user = user
				
	#getter methods
	def get_is_liked_interaction():
		return self.is_liked_interaction

	def get_is_disliked_interaction():
		return self.is_disliked_interaction

	def get_is_comment_interaction():
		return self.is_comment_interaction

	def get_is_follow_interaction():
		return self.is_follow_interaction

	def get_time():
		return self.time

	def get_text():
		return self.text

	def get_user():
		return self.user

	def get_object_interacted_with():
		return self.object_interacted_with

	#general methods
	def to_string():
		return get_text()

