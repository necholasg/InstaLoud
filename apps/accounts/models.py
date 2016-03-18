from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime

class Post(models.Model):
    caption = models.CharField(max_length = 150)
    artist = models.CharField(max_length = 30)
    title = models.CharField(max_length = 50)
    song_url = models.URLField(max_length=355)
    album_art = models.URLField(max_length=355)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    class Meta:
        db_table = 'posts'
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    def __str__(self):
			return self.caption

class Comment(models.Model):
    content = models.CharField(max_length = 240)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    class Meta:
        db_table = 'comments'
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
    def __str__(self):
			return self.content

class Like(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    class Meta:
        db_table = 'likes'
        verbose_name = "Like"
        verbose_name_plural = "Likes"
        unique_together = ('post','user')
    def __str__(self):
			return self.post.caption + self.user.username

class Notification(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)
    like = models.ForeignKey(Like)
    class Meta:
        db_table = 'notifications'
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
    def __str__(self):
			return self.post+self.like
    
class Follower(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User,related_name="creator")
    follower = models.ForeignKey(User,related_name="follower")
    class Meta:
        db_table = 'followers'
        unique_together = ('creator', 'follower')
        verbose_name = "Follower"
        verbose_name_plural = "Followers"
    def __str__(self):
			return self.creator.username
    
    

    
