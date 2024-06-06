from django.contrib import admin
from django.urls import path,include
from django.conf import settings
# from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from app_login import views


app_name='app_login'
urlpatterns = [
    path('signup/',views.sign_up,name='signup' ),
    path('login/',views.login_page,name='login' ),
    path('profile/',views.edit_profile,name='profile' ),
    
]
