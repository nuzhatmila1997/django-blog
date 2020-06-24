from django.db import models
from django.contrib.auth.models import User #username, password, email, first_name,last_name

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name='user_profile',on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics')
