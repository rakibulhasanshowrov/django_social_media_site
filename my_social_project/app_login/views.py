from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from app_login.forms import CreateNewUser,LoginUserForm
from django.urls import reverse_lazy,reverse
from app_login.models import UserProfile
from django.contrib.auth.decorators import login_required
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
            pass
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
                return render(request,'app_login/profile.html')
    return render(request,"app_login/login.html",context=dict)
    
@login_required           
def edit_profile(request):
    current_user=request.user
    profile=UserProfile.objects.get(user=current_user)
    dict={
        'title':'Edit Profile',
        "user":profile,
    }
    return render(request,'app_login/profile.html',context=dict)
              