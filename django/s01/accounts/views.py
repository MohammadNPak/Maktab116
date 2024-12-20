from django.shortcuts import render
# from django.contrib.auth.models import User
from accounts.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from .forms import RegisterForm,UserUpdateForm,MyUserCreationForm
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse("blog"))
        else:
            messages.add_message(request, messages.ERROR,
                                 "invalid username or password")
            return render(request, 'accounts/login.html', context={})

    elif request.method == "GET":
        return render(request, 'accounts/login.html', context={})


# def validate_username(username):
#     return len(username)>=8

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"])

            messages.add_message(
                request,
                messages.SUCCESS,
                f"congras {form.cleaned_data['username']}! you have successfully registered in our site")
            return redirect(reverse("blog"))
        else:
            return render(request, "accounts/register.html", context={"form": form})
    elif request.method == "GET":
        form = UserCreationForm()
        return render(request, "accounts/register.html", context={"form": form})


def logout_view(request):
    logout(request)
    return redirect(reverse("index"))


class RegisterView(CreateView):
    form_class=MyUserCreationForm
    model=User
    template_name="accounts/register.html"
    success_url="/accounts/login"


# @login_required
# def upload_picture(request):
#     if request.method=="GET":
#         form =UserUpdateForm() 
#         return render(request,"accounts/upload_picture.html",{"form":form})
    
#     elif request.method=="POST":
#         user = request.user
#         form = UserUpdateForm(request.POST,request.FILES,instance=user)
#         if form.is_valid():
#             form.save()
#         return redirect(reverse("post_list"))

class UserPictureUpdateView(LoginRequiredMixin,UpdateView):
    model=User
    fields=("picture",)
    login_url="/accounts/login/"
    
    # def get_permission_denied_message(self):
        
    #     return super().get_permission_denied_message()
    
    def get_object(self, queryset = ...):
        
        obj = self.get_queryset().get(pk=self.kwargs[self.pk_url_kwarg])
        if self.request.user != obj:
            raise PermissionError("you cant upload picture for another accounts")
        else:
            return obj
    
