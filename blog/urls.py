__author__ = "Agentbree21"
from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from blog import views as blog_views

urlpatterns = [
	url(r'^posts/$', views.post_list, name='posts'),
	url(r'^$',views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^teampair/$', views.team, name='team'),
	url(r'^register/$', views.register_page, name='register'),
	url(r'^login/$', views.login, name ='login'),
	url(r'^post/$', views.addPost, name ='post'),
	url(r'^logout/$', views.signout, name ='signout'),



	


]

