from django.contrib import admin
from .models import Post

# class PostTabular(admin.TabularInline):
#     model=Post


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    # fields = ["title","body"]
    pass

