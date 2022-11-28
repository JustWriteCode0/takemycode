from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .services import registration, user_login, profiles


def user_registration(request):
    return registration(request)


def authenticate(request):
    return user_login(request)


def user_logout(request):
    logout(request)
    return redirect('/')


@login_required
def user_profiles(request, user_name):
    return profiles(request, user_name)