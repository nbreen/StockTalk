#!/usr/bin/env python
# coding: utf-8

#imports
from User import User
from Post import Post
from Comment import Comment
from Interaction import Interaction
from Topic import Topic
from Timeline import Timeline

u1 = User()
u1.set_username("Kelly")
print(u1.get_username())
u2 = User()
u2.set_username("Jim")

p1 = Post()
p1.set_author(u2)
p2 = Post()
p3 = Post()

print(p1.get_id())
print(p2.get_id())
print(p3.get_id())

u1.dislike_post(p1)
u1.like_post(p1)
u1.add_post("some post text", None, None)

for interaction in u1.get_interactions():
	print(interaction.to_string())

print(p1.get_dislikes())


for post in u1.get_posts():
	print(post.to_string())
