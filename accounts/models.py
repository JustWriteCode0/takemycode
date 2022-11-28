from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ImageField
from django.dispatch import receiver
from django.db.models.signals import post_save



class UserCustom(AbstractUser):
    '''User model for registration'''
    username = models.CharField(max_length=50, unique=True)
    user_avatar = models.ImageField(default="avatar/default.png", upload_to="avatar/", blank=True, null=True)
    email = models.EmailField(max_length=55, unique=True)
    join_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username


class Profile(models.Model):    
    profile = models.OneToOneField(UserCustom, verbose_name='Пользователь' ,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    describe = models.TextField(null=True, blank=True)
    github = models.URLField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.profile.username


    @receiver(post_save, sender=UserCustom) 
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(profile=instance)
            

    @receiver(post_save, sender=UserCustom)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()