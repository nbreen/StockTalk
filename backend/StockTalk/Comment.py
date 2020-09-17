#!/usr/bin/env python
# coding: utf-8

#imports
from datetime import date

#Comment class
class Comment:
	
	#variables
	def __init__(self):
		self.likes = 0
		self.dislikes = 0
		self.author = None
		self.post = None
		self.text = ""

		#set time
		current_time = datetime.now()
		self.time = current_time.strftime("%d/%m/%Y %H:%M:%S")
	
	#setter methods
	def set_author(author):
		self.author = author

	def set_post(post):
		self.post = post

	def set_text(text):
		self.text = text
	
	#getter methods
	def get_author():
		return self.author

	def get_likes():
		return self.likes

	def get_dislikes():
		return self.dislikes

	def get_post():
		return self.post

	def get_text():
		return self.text

	def get_time():
		return self.time

	#general methods
	def increment_likes():
		self.likes += 1

	def decrement_likes():
		self.likes -= 1

	def increment_dislikes():
		self.dislikes += 1

	def decrement_dislikes():
		self.likes -= 1

	def to_string():
		return "a comment made by " + author.to_string())

