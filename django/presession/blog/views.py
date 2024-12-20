from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from django.contrib.postgres.search import SearchQuery,SearchRank,SearchVector
from django.db.models import Func,F



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


class Headline(Func):
    function='ts_headline'
    template = "%(function)s(%(expressions)s,%(search_query)s)"

class SearchResultView(ListView):
    model=Post
    context_object_name='post_objects'
    template_name='blog/search_result.html'
    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            search_vector = SearchVector('title','body','author__username')
            search_query = SearchQuery(q)
            return (Post.objects
                    .annotate(rank=SearchRank(search_vector,search_query),
                              hl_title=Headline(F('title'),search_query),
                              hl_body=Headline(F('body'),search_query),
                              hl_username=Headline(F('author__username'),search_query),
                              )
                    .filter(rank__gte=0.001)
                    .order_by('-rank'))
        
        return Post.objects.none()
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

