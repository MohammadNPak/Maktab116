from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
<<<<<<< HEAD
from django.views.generic import CreateView,UpdateView,ListView
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse

from django.contrib.postgres.search import SearchQuery,SearchRank,SearchVector
from django.db.models import Func,F
=======
from django.views.generic import CreateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

>>>>>>> 89a7a0ed935605cb33d82b45e3dfd52be86f1efa

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
    

<<<<<<< HEAD
class CreateCommentView(LoginRequiredMixin,CreateView):
    model=Comment
    fields=("body",)
    # success_url=
    
    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.author = self.request.user
        post =get_object_or_404(Post,pk=self.kwargs.get('pk'))
        self.object.parent = post
        self.object.save()
        # do something with self.object
        # remember the import: from django.http import HttpResponseRedirect
        return HttpResponseRedirect(reverse('post_detail',kwargs={"pk":self.kwargs.get('pk')}))
    

class LikePost(LoginRequiredMixin,View):

    def post(self,request,*args, **kwargs):
        # print(request)
        post = get_object_or_404(Post,pk=self.kwargs.get("pk"))
        if post.like.filter(pk=request.user.id).exists():
            post.like.remove(request.user)
        else:
            post.like.add(request.user)

        # post.save()

        return redirect(reverse_lazy("post_list"))

class Highligh(Func):
    function = 'ts_headline'
    template="%(function)s('%(expressions)s','%(search_query)s')"


class SearchResultsView(ListView):
    
    template_name='blog/search_results.html'
    context_object_name='post_objects'

    def get_queryset(self):
        q = self.request.GET.get('search_query')
        if q:
            search_query = SearchQuery(q)
            search_vector = SearchVector('title','body','author__username')

            return (Post.objects
                    .annotate(
                        rank=SearchRank(search_vector,search_query),
                        hl_body=Highligh(F('body'),search_vector),
                        hl_title=Highligh(F('title'),search_vector),
                        )
                    .filter(rank__gte=0.01).order_by('-rank')
                    )
        # Post.objects.filter(body=F('title'))

        return Post.objects.none()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search_query')
        return context
    

        # do_somthing() -> do_somthing 
        # do_somthing(first_arg) -> do_somthing
        # 
        # class person:
        #   name=mohammad       -> person.name
        # 
        # d = {'name':"mohammad"}  -> d.name
=======
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
    
>>>>>>> 89a7a0ed935605cb33d82b45e3dfd52be86f1efa
