#!/usr/bin/env python
# coding: utf-8

#imports
#install PIL using "pip install Pillow" in cmd
from PIL import Image
import Comment
import Interaction
import Timeline
import Topic
import Post
import re
import csv


#User class
class User:
    
	#variables
	def __init__(self):
		self.username = ""
		self.email = ""
		self.password = ""
		self.name = ""
		self.bio = ""
		self.profile_image = Image.open("img/default_profile_pic.jpg")
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
		self.investments[investment] = value

	def follow_user(self, user):
		if user not in self.following:
			self.following.append(user)

	def unfollow_user(self, user):
		if user in self.following:
			self.following.remove(user)

	def log_in(self):
		self.is_logged_in = True

	def log_out(self):
		self.is_logged_in = False

	def delete_account(self):
		#implement later
		pass

	#check if post has a valid topic
	def check_for_topic(self, text):
		potential_topic = re.findall(r"#(\w+)",text)
		with open("valid_tickers.csv", "r") as f:
			reader = csv.reader(f, delimiter=',')
			for row in reader:
				for field in row:
					if field == potential_topic[0]:
						f.close()
						return potential_topic[0]
		f.close()
		return None
		
	#pass 'None' to image and/or topic if not used. Pass an empty string "" to text if image
	def add_post(self, text, image):
		#create new post
		new_post = Post.Post()
		new_post.set_author(self)
		#if is image post
		if image is not None:
			new_post.set_is_image()
			new_post.set_post_image(image)
		#else if is text post
		else:
			new_post.set_post_text(text)
		
		#set topic if given
		topic = self.check_for_topic(text)
		if topic is not None:
			new_post.set_topic(topic)
			self.topics_used.append(topic)

			#update recent topics used by user
			if len(self.recent_topics) > self.NUMBER_OF_RECENT_TOPICS_TO_TRACK:
				del self.recent_topics
				self.recent_topics.append(topic)
			else:
				self.recent_topics.append(topic)

		#add to posts
		self.posts.append(new_post)

		#record interaction
		new_interaction = Interaction.Interaction()
		new_interaction.set_user(self)
		new_interaction.set_post_interacted_with(new_post)
		new_interaction.set_is_post_interaction()
		new_interaction.set_text()
		self.add_interaction(new_interaction)


	def remove_post(self, post):
		self.posts.remove(post)
	
	#dislike post - if it is already disliked by the user then it will un-dislike it (no interaction recorded). User can't dislike and like a post.
	def dislike_post(self, post):
		#check if user already liked post
		if self in post.users_liked:
			post.remove_user_liked(self)
			post.add_user_disliked(self)
			post.decrement_likes()
			post.increment_dislikes()

			#record interaction
			new_interaction = Interaction.Interaction()
			new_interaction.set_user(self)
			new_interaction.set_post_interacted_with(post)
			new_interaction.set_is_disliked_interaction()
			new_interaction.set_text()
			self.add_interaction(new_interaction)

		#check if user already disliked post
		elif self in post.users_disliked:
			post.decrement_dislikes()
			post.remove_user_disliked(self)

		#standard dislike
		else:
			post.increment_dislikes()
			post.add_user_disliked(self)

			#record interaction
			new_interaction = Interaction.Interaction()
			new_interaction.set_user(self)
			new_interaction.set_post_interacted_with(post)
			new_interaction.set_is_disliked_interaction()
			new_interaction.set_text()
			self.add_interaction(new_interaction)
			
	#like post - if it is already disliked by the user then it will un-like it (no interaction recorded). User can't dislike and like a post.
	def like_post(self, post):
		#check if user already disliked post
		if self in post.users_disliked:
			post.remove_user_disliked(self)
			post.add_user_liked(self)
			post.increment_likes()
			post.decrement_dislikes()

			#record interaction
			new_interaction = Interaction.Interaction()
			new_interaction.set_user(self)
			new_interaction.set_post_interacted_with(post)
			new_interaction.set_is_liked_interaction()
			new_interaction.set_text()
			self.add_interaction(new_interaction)

		#check if user already liked post
		elif self in post.users_liked:
			post.decrement_likes()
			post.remove_user_liked(self)

		#standard like
		else:
			post.increment_likes()
			post.add_user_liked(self)

			#record interaction
			new_interaction = Interaction.Interaction()
			new_interaction.set_user(self)
			new_interaction.set_post_interacted_with(post)
			new_interaction.set_is_liked_interaction()
			new_interaction.set_text()
			self.add_interaction(new_interaction)

		#dislike comment - if it is already disliked by the user then it will un-dislike it (no interaction recorded). User can't dislike and like a comment.
	def dislike_comment(self, comment):
		#check if user already liked comment
		if self in comment.users_liked:
			comment.remove_user_liked(self)
			comment.add_user_disliked(self)
			comment.decrement_likes()
			comment.increment_dislikes()

			#record interaction
			new_interaction = Interaction.Interaction()
			new_interaction.set_user(self)
			new_interaction.set_comment_interacted_with(comment)
			new_interaction.set_is_disliked_interaction()
			new_interaction.set_text()
			self.add_interaction(new_interaction)

		#check if user already disliked comment
		elif self in comment.users_disliked:
			comment.decrement_dislikes()
			comment.remove_user_disliked(self)

		#standard dislike
		else:
			comment.increment_dislikes()
			comment.add_user_disliked(self)

			#record interaction
			new_interaction = Interaction.Interaction()
			new_interaction.set_user(self)
			new_interaction.set_comment_interacted_with(comment)
			new_interaction.set_is_disliked_interaction()
			new_interaction.set_text()
			self.add_interaction(new_interaction)
			
	#like comment - if it is already disliked by the user then it will un-like it (no interaction recorded). User can't dislike and like a comment.
	def like_comment(self, comment):
		#check if user already disliked comment
		if self in comment.users_disliked:
			comment.remove_user_disliked(self)
			comment.add_user_liked(self)
			comment.increment_likes()
			comment.decrement_dislikes()

			#record interaction
			new_interaction = Interaction.Interaction()
			new_interaction.set_user(self)
			new_interaction.set_comment_interacted_with(comment)
			new_interaction.set_is_liked_interaction()
			new_interaction.set_text()
			self.add_interaction(new_interaction)

		#check if user already liked comment
		elif self in comment.users_liked:
			comment.decrement_likes()
			comment.remove_user_liked(self)

		#standard like
		else:
			comment.increment_likes()
			comment.add_user_liked(self)

			#record interaction
			new_interaction = Interaction.Interaction()
			new_interaction.set_user(self)
			new_interaction.set_comment_interacted_with(comment)
			new_interaction.set_is_liked_interaction()
			new_interaction.set_text()
			self.add_interaction(new_interaction)


	def follow_topic(self, topic):
		if topic not in self.topics_following:
			self.topics_following.append(topic)

	def unfollow_topic(self, topic):
		if topic in self.topics_following:
			self.topics_following.remove(topic)
	
	def add_saved_post(self, post):
		if post not in self.saved_posts:
			self.saved_posts.append(post)

	def remove_saved_post(self, post):
		if post in self.saved_posts:
			self.saved_posts.remove(post)

	def add_interaction(self, interaction):
		self.interactions.append(interaction)

	def add_comment(self, post, text):
		#add new comment
		new_comment = Comment.Comment()
		new_comment.set_author(self)
		new_comment.set_post(post)
		new_comment.set_text(text)
		post.add_comment(new_comment)

		#record interaction
		new_interaction = Interaction.Interaction()
		new_interaction.set_user(self)
		new_interaction.set_post_interacted_with(post)
		new_interaction.set_is_comment_interaction()
		new_interaction.set_text()
		self.add_interaction(new_interaction)

	#no interaction recorded for removing comment
	def remove_comment(self, post, comment):
		post.remove_comment(comment)

	def to_string(self):
		return self.get_username()



