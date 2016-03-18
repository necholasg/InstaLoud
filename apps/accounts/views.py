from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import forms, login, authenticate, logout
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegisterForm, LoginForm, AddForm
from .models import Post, Comment, Like, Notification, Follower
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core import serializers
import json


class Index(View):
    form_reg = RegisterForm
    form_login = LoginForm
    def get(self, request):
        if request.user.is_authenticated():
            ids = [request.user.id]
            following = Follower.objects.all().filter(follower = request.user)
            
            for x in following:
                ids.append(x.creator.id)
            creators_posts= Post.objects.all().filter(user__in = ids).order_by('-id')
            posts_ids = []
            for post in creators_posts:
                posts_ids.append(post.id)
            comments = Comment.objects.all().filter(post__in = posts_ids).order_by('id')
            user_likes = Like.objects.all().filter(user = request.user)
            user_likes_ids = []
            for like in user_likes:
                user_likes_ids.append(like.post.id)
            posts_like = Like.objects.all().filter(post__in = posts_ids)
            like_counter = {}
            for like in posts_like:
                if like.post.id not in like_counter:
                    like_counter[like.post.id] = 1
                else:
                    like_counter[like.post.id] += 1
            context = { 'creators_posts' : creators_posts, 'comments' : comments, 'liked_posts' : user_likes_ids, 'like_counter': like_counter };
            return render(request, 'accounts/main.html', context)
        else:
     		context = {'form_reg' : self.form_reg(), 'form_login' : self.form_login()}
     		return render(request, 'accounts/index.html', context)

class Register(View):
	form_reg = RegisterForm
	form_login = LoginForm
	def post(self, request):
		form_reg = self.form_reg(request.POST)
		context = {'form_reg': form_reg, 'form_login' : self.form_login}
		if form_reg.is_valid():
			form_reg.save()
			return redirect('/')
		else:
		    context['reg_error'] = True
		    return render(request, 'accounts/index.html', context)
		    
class Login(View):
    form_reg = RegisterForm
    form_login = LoginForm

    def post(self, request):
        form_login = self.form_login(None,request.POST)
        context = {'form_login' : form_login, 'form_reg': self.form_reg}

        if form_login.is_valid():
            username = form_login.cleaned_data['username']
            password = form_login.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                context['login_error'] = True
                return render(request, 'accounts/index.html', context)
        else:
            context['login_error'] = True 
            # print form_login.errors
            # print form_login.non_field_errors
            # print context
            return render(request, 'accounts/index.html', context)

class Logout(View):
	def get(self, request):
		logout(request)
		return redirect('/')
		
class Search(View):
    def get(self, request):
        return render(request, 'accounts/search.html')
        
class Search_profile(View):
    def get(self, request):
        return render(request, 'accounts/search_profile.html')
    def post(self, request):
        q = User.objects.filter(username__contains = request.POST["profile"])
        if len(q) < 1:
            q = "<h1>Sorry, that user could not be found :( Please search again</h1>"
            
        json_data = serializers.serialize('json', q)
        return HttpResponse(json_data, content_type='application/json')
        
    
    

class Add(View):
    form = AddForm
    
    def get(self, request):
        context = {'form' : self.form()}
        return render(request, 'accounts/add_post.html',context)

    def post(self, request):
        if 'add_song' in request.POST:
            form = self.form(initial={'song_url':request.POST['add_song']})
            context = {'form' : form}
            return render(request, 'accounts/add_post.html',context)
        
        form = self.form(None or request.POST)
        context = {'form' : form}
        current_user = User.objects.get(id=self.request.user.id)
        if form.is_valid():
            title = form.cleaned_data['title']
            artist = form.cleaned_data['artist']
            song_url = form.cleaned_data['song_url']
            album_art = request.POST['album_art']
            caption = form.cleaned_data['caption']
            user = current_user
            Post.objects.create(title = title, artist = artist, song_url = song_url, caption = caption, user = user, album_art = album_art)
            return redirect('/')
        else:
            return render(request, 'accounts/add_post.html', context)
    
class Profile(View):
    def get(self, request, username):
        alias = self.kwargs['username']
        user_now = User.objects.get(username = alias)
        page_followers = Follower.objects.all().filter(creator = user_now)
        followers = len(Follower.objects.all().filter(creator = user_now))
        following = len(Follower.objects.all().filter(follower = user_now))
        posts = Post.objects.all().filter(user = user_now).order_by('-id')
        posts_ids = []
        for post in posts:
            posts_ids.append(post.id)
        comments = Comment.objects.all().filter(post__in = posts_ids).order_by('id')
        status = False
        
        for x in page_followers:
            if request.user.username == x.follower.username:
                status = True
        user_likes = Like.objects.all().filter(user = request.user)
        user_likes_ids = []
        for like in user_likes:
            user_likes_ids.append(like.post.id)
        posts_like = Like.objects.all().filter(post__in = posts_ids)
        like_counter = {}
        for like in posts_like:
            if like.post.id not in like_counter:
                like_counter[like.post.id] = 1
            else:
                like_counter[like.post.id] += 1
        context = {
            "posts" : posts,
            "posts_count" : len(posts),
            "profile" : user_now,
            "followers" : followers,
            "following" : following,
            "comments" : comments,
            "status" : status,
            'liked_posts' : user_likes_ids,
            'like_counter' : like_counter,
            }
            
        return render(request, 'accounts/profile.html', context)

class Follow(View):
    def get(self, request, creator_id):
        creator_id = self.kwargs['creator_id']
        follower = User.objects.get(id = request.user.id)
        creator = User.objects.get(id = creator_id)
        Follower.objects.create(creator = creator, follower = follower)
        data = json.dumps({"message":"success"})
        
        # json_data = serializers.serialize('json', data)
        return HttpResponse(data)

class Comment_main(View):
    def post(self, request):
        content = request.POST['comment']
        post_id = request.POST['post_id']
        post = Post.objects.get(id=post_id)
        user = User.objects.get(id=request.user.id)
        Comment.objects.create(content=content, post=post, user=user)
        data = Comment.objects.all().filter(post=post_id)
        json_data = serializers.serialize('json', data)
        return HttpResponse(json_data, content_type='application/json')
        

class New_like(View):
    def post(self,request):
        post = Post.objects.get(id = request.POST['post_id'])
        user = User.objects.get(id=request.user.id)
        Like.objects.create(post = post, user=user)
        data = json.dumps({"message":"success"})
        return HttpResponse(data)
        
        
        