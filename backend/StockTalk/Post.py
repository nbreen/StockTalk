#!/usr/bin/env python
# coding: utf-8

#imports
#install PIL using "pip install Pillow" in cmd
from PIL import Image

#Post class
class Post:

	#static id variable
	post_id = 0

	#variables
	def __init__(self):
		self.is_image = False
		self.post_text = ""
		self.post_image = Image.open("TODO: insert default post image path here")
		self.author = None
		self.likes = 0
		self.dislikes = 0
		self.topic = None
		self.comments = []

		#set time
		current_time = datetime.now()
		self.time = current_time.strftime("%d/%m/%Y %H:%M:%S")

		#update post id
		post_id += 1
	
	#setter methods
	def set_is_image()
		self.is_image = True

	def set_post_text(post_text)
		self.post_text = post_text

	def set_post_image(post_image)
		self.post_image = post_image	

	def set_author(author)
		self.author = author	

	def set_topic(topic)
		self.topic = topic	

	#getter methods
	def get_text():
		return self.post_text

	def get_image():
		return self.post_image

	def get_author():
		return self.author

	def get_likes():
		return self.likes

	def get_dislikes():
		return self.dislikes

	def get_topic():
		return self.topic

	def get_comments():
		return self.comments

	def get_id():
		return post_id

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

	def add_comment(comment):
		self.comments.append(comment)

	def remove_comment(comment):
		self.comments.remove(comment)

	def to_string():
		return "a post made by " + author.to_string())

