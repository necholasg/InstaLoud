from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from .models import Post
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(min_length = 2)
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', help_text=None, min_length=3)
    first_name = forms.CharField(label='First Name',min_length = 2)
    last_name = forms.CharField(label='Last Name',min_length = 2)
    email = forms.EmailField(label='Email Address')
    password2 = forms.CharField(label='Confirm Password', help_text=None, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            return user
            
class AddForm(ModelForm):
    caption = forms.CharField( widget=forms.Textarea(attrs={'placeholder': 'Caption'}),required=False)
    artist = forms.CharField(required = False)
    title = forms.CharField(max_length = 50, min_length = 3, required = True)
    song_url = forms.URLField(max_length=355, required = False)
    url_status = forms.BooleanField(initial = False, required = True, error_messages={'required': 'Please check your submitted url.'})
    class Meta:
        model = Post
        fields = ('caption','artist','title','song_url')
    def save(self, commit=True):
        post = super(AddForm, self).save(commit=False)
        post.caption = self.cleaned_data['caption']
        post.artist = self.cleaned_data['artist']
        post.title = self.cleaned_data['title']
        post.song_url = self.cleaned_data['song_url']
        if commit:
            post.save()
            return post
    


