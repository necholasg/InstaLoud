from django.conf.urls import url, patterns, include
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$',views.Index.as_view(), name='index'),
    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),
    url(r'^search/$', views.Search.as_view(), name='search'),
    url(r'^add/$', views.Add.as_view(), name='add'),
    url(r'^search_profile/$', views.Search_profile.as_view(), name='search_profile'),
    url(r'^profile/(?P<username>[\w]+)/$', views.Profile.as_view(), name='profile'),
    url(r'^follow/(?P<creator_id>[\d]+)/$', views.Follow.as_view(), name='follow'),
    url(r'^comment/$', views.Comment_main.as_view(), name='comment_main'),
    url(r'^like/$', views.New_like.as_view(), name='like'),
]
