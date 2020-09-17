#!/usr/bin/env python
# coding: utf-8

#imports
#install PIL using "pip install Pillow" in cmd
from PIL import Image

#User class
class User:
    
	#variables
	def __init__(self):
		self.username = ""
		self.email = ""
		self.password = ""
		self.name = ""
		self.bio = ""
		self.profile_image = Image.open("Generic-Person-Image-for-Signatures.jpg")
		self.stock_interests = []
		self.investments = {}
		self.followers = []
		self.following = []
		self.is_logged_in = False
		self.posts = []
		self.topics_used = []
		self.topics_following = []
		self.saved_posts = []
		self.interactions = []
		self.recent_topics = []
        
		#constant variables
		self.NUMBER_OF_RECENT_TOPICS_TO_TRACK = 10
		
	#setter methods
	def set_username(self, username):
		self.username = username

	def set_email(self, email):
		self.email = email

	def set_password(self, password):
		self.password = password

	def set_name(self, name):
		self.name = name

	def set_bio(self, bio):
		self.bio = bio

	def set_profile_image(self, profile_image):
		self.profile_image = Image.open(profile_image)

	def set_stock_interests(self, stock_interests):
		self.stock_interests = stock_interests

	#getter methods
	def get_username(self):
		return self.username

	def get_email(self):
		return self.email

	def get_password(self):
		return self.password

	def get_name(self):
		return self.name

	def get_bio(self):
		return self.bio

	def get_profile_image(self):
		return self.profile_image

	def get_stock_interests(self):
		return self.stock_interests

	def get_investments(self):
		return self.investments
	
	def get_posts(self):
		return self.posts

	def get_recent_topics(self):
		return self.recent_topics

	def get_topics_following(self):
		return self.topics_following

	def get_saved_posts(self):
		return self.saved_posts

	def get_interactions(self):
		return self.interactions
	

	#general methods
	def edit_investments(self, investment, value):
		self.investment[investment] = value

	def follow_user(self, user):
		self.following.append(user)

	def unfollow_user(self, user):
		self.following.remove(user)

	def log_in(self):
		self.is_logged_in = True

	def log_out(self):
		self.is_logged_in = False

	def delete_account(self):
		#implement later
		pass

	def add_post(self, post):
		self.posts.append(post)

	def remove_post(self, post):
		self.posts.remove(post)
	
	def dislike_post(self, post):
		#implement later
		pass
	
	def like_post(self, post):
		#implement later
		pass
	
	def follow_topic(self, topic):
		self.topics_following.append(topic)

	def unfollow_topic(self, topic):
		self.topics_following.remove(topic)

	def update_recent_topics(self, topic):
		if len(self.recent_topics > self.NUMBER_OF_RECENT_TOPICS_TO_TRACK):
			del self.recent_topics[0]
			self.recent_topics.append(topic)
		else:
			self.recent_topics.append(topic)
	
	def add_saved_post(self, post):
		self.saved_posts.append(post)

	def remove_saved_post(self, post):
		self.saved_posts.remove(post)

	def add_interaction(self, interaction):
		self.interactions.append(interaction)

	def add_comment(self, comment):
		#implement later
		pass

	def remove_comment(self, comment):
		#implement later
		pass

	def to_string(self):
		return self.get_username()



