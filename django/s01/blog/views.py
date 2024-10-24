from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def posts_list_view(request):
    if request.method=="GET":
        p = Post.objects.all()
        return render(request,'blog/posts.html'
                    ,context={"post_objects":p})
    elif request.method=="POST":
        user=request.user
        title = request.POST.get("title")
        body = request.POST.get("body")
        Post.objects.create(author=user,title=title,body=body)
        p = Post.objects.all().order_by("-created_at")
        messages.add_message(request,messages.SUCCESS,"your Post was added successfully!")        
        return render(request,'blog/posts.html'
                    ,context={"post_objects":p})

def post_detail_view(request,pk):
    if request.method=="GET":
        p = get_object_or_404(Post,pk=pk)
        return render(request,'blog/post_detail.html',context={"post":p})
    

class CreateCommentView(LoginRequiredMixin,CreateView):
    model=Comment
    fields=("body",)
    
    