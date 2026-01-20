from django.contrib import admin
from .models import Post

#we can register our models here so we can see them in the admin page
admin.site.register(Post)