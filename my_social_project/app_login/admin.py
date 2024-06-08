from django.contrib import admin
from app_login.models import UserProfile,Follow
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Follow)