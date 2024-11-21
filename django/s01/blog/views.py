from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin


@login_required
# @permission_required()
def posts_list_view(request):
    if request.method=="GET":
        p = Post.objects.all()
        return render(request,'blog/posts.html'
                    ,context={"post_objects":p})
    elif request.method=="POST":
        user=request.user
        if not user.has_perm("blog.add_post"):
            raise PermissionError("you dont have permission to create post")
        
        title = request.POST.get("title")
        body = request.POST.get("body")
        Post.objects.create(author=user,title=title,body=body)
        p = Post.objects.all().order_by("-created_at")
        messages.add_message(request,messages.SUCCESS,"your Post was added successfully!")        
        return render(request,'blog/posts.html'
                    ,context={"post_objects":p})

def post_detail_view(request,pk):
    if request.method=="GET":
        
        post=get_object_or_404(Post,id=pk)
        ct =ct = ContentType.objects.get_for_model(Post)
        comments = Comment.objects.filter(content_type=ct,object_id=pk)
        return render(request,"blog/post_detail.html",context={'comments':comments,"post":post})
    

class CreateCommentView(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required="blog.can_add_comment"
    def post(self,request,content_type,object_id):
        body = request.POST.get("body")
        ct = ContentType.objects.get(
            model=content_type)
        comment=Comment.objects.create(author=self.request.user,
                               body=body,
                               content_type=ct,
                               object_id=object_id)
        return HttpResponse(200)
    
