from django.contrib import admin
from .models import Post
from accounts.models import User
from django.contrib.auth.admin import UserAdmin 

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    # fields = ["title","body"]
    pass

@admin.register(User)
class UserModelAdmin(UserAdmin):
    pass
