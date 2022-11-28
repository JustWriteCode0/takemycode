from django.shortcuts import render, redirect

from .services import add_post, home_page, like_post


def post_likes(request, pk):
    return like_post(request, pk)

def main_page(request):
    return home_page(request)

def create_post(request):
    return add_post(request)
