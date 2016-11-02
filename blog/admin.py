from django.contrib import admin
#Import the userProfile model individually.

# Register your models here.
from .models import Post
admin.site.register(Post)