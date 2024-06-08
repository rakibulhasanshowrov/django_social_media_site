from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_profile')
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)
    dob=models.DateField(blank=True,null=True)
    website=models.URLField(blank=True)
    facebook=models.URLField(blank=True)
    
    def __str__(self):
        return self.user.username
    