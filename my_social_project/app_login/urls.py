from django.contrib import admin
from django.urls import path,include
from django.conf import settings
# from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from app_login import views


app_name='app_login'
urlpatterns = [
    path('signup/',views.sign_up,name='signup' ),
    path('login/',views.login_page,name='login' ),
    path('profile/',views.profile,name='profile' ),
    path('logout/',views.logout_user,name='logout' ),
    path('edit-profile/',views.edit_profile,name='edit_profile' ),
    path('user/<username>/',views.user,name='user'),
    path('follow/<username>/',views.follow,name='follow'),
    path('unfollow/<username>/',views.unfollow,name='unfollow'),
    
]
