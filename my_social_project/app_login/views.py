from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from app_login.forms import CreateNewUser,LoginUserForm,EditProfileForm
from django.urls import reverse_lazy,reverse
from app_login.models import UserProfile,Follow
from django.contrib.auth.decorators import login_required
from app_post.forms import PostForm
from django.contrib.auth.models import User
# Create your views here.

def sign_up(request):
    form = CreateNewUser()
    dict={
        'form':form,
        'title':'SignUp',
    }
    if request.method=="POST":
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user=form.save()
            dict.update({'form':form,'registered':True})
            user_profile=UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('app_login:login'))
        else:
            dict.update({'form':form,'registered':False})
    return render(request,'app_login/signup.html',context=dict)

def login_page(request):
    form=LoginUserForm()
    dict={
        'form':form,
        'title':'Login',
    }
    if request.method=="POST":
        form=LoginUserForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('app_post:home'))
    else:
        return render(request,"app_login/login.html",context=dict)
    
@login_required           
def edit_profile(request):
    current_user=UserProfile.objects.get(user=request.user)
    form=EditProfileForm(instance=current_user)
    if request.method=="POST":
        form=EditProfileForm(request.POST,request.FILES,instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form=EditProfileForm(instance=current_user)
            return HttpResponseRedirect (reverse('app_login:profile'))
    
    return render(request,'app_login/profile.html',context={'title':'Edit Profile',
        "form":form,})


@login_required
def logout_user(request):
        logout(request)
        return HttpResponseRedirect(reverse('app_login:login'))
    
@login_required
def profile(request):
    form=PostForm()
    if request.method =="POST":
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return HttpResponseRedirect(reverse('home'))
    
    return render(request,'app_login/user.html',context={'title':'User','form':form})

@login_required
def user(request,username):
    user_other=User.objects.get(username=username)
    already_followed=Follow.objects.filter(follower=request.user,following=user_other)
    if user_other==request.user:
        return HttpResponseRedirect(reverse('app_login:profile'))
    return render(request,'app_login/user_other.html',context={'user_other':user_other ,'already_followed': already_followed})
    

@login_required
def follow(request,username):
    following_user=User.objects.get(username=username)
    follower_user=request.user
    already_followed=Follow.objects.filter(follower=follower_user,following=following_user)
    if not already_followed:
        followed_user=Follow(follower=follower_user,following=following_user)
        followed_user.save()
    return HttpResponseRedirect (reverse('app_login:user',kwargs={'username':username}))

@login_required
def unfollow(request,username):
    following_user=User.objects.get(username=username)
    follower_user=request.user
    already_followed=Follow.objects.filter(follower=follower_user,following=following_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('app_login:user',kwargs={'username':username}))