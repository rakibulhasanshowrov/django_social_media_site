from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    dict={
        'title':"Home Page",
    }
    return render (request,'app_post/home.html',context=dict)