from django.contrib import admin

from .models import Post, Comment, Like, Notification, Follower 

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Notification)
admin.site.register(Follower)

