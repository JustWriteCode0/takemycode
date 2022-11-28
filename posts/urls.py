from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
    path('', main_page, name="home_page"),
    path('create-post', create_post, name="create_post"),
    path('like<int:pk>', post_likes, name="like_post"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
