from django.shortcuts import render
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app_login.models import UserProfile,Follow
from app_post.models import Posts,Like
from django.urls import reverse_lazy,reverse

# Create your views here.
@login_required
def home(request):
    following_list=Follow.objects.filter(follower=request.user)
    posts=Posts.objects.filter(author__in=following_list.values_list("following"))
    if request.method=="GET":
        search=request.GET.get('search','')
        result=User.objects.filter(username__icontains=search)
    return render (request,'app_post/home.html',context={'title':'Home', "search":search,'result':result,'following_list':following_list,'posts':posts})

@login_required
def liked(request,pk):
    post=Posts.objects.get(pk=pk)
    already_liked=Like.objects.filter(post=post,user=request.user)
    if not already_liked:
        liked_post=Like(post=post,user=request.user)
        liked_post.save()
    return HttpResponseRedirect(reverse('home'))


@login_required
def unliked(request,pk):
    post=Posts.objects.get(pk=pk)
    already_liked=Like.objects.filter(post=post,user=request.user)   
    already_liked.delete()
    return HttpResponseRedirect(reverse('home'))     
    