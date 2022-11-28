from accounts.models import UserCustom
from django.db import models


class Publication(models.Model):
    author = models.ForeignKey(UserCustom, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    content = models.TextField()
    link = models.URLField(null=True, blank=True)
    images = models.ImageField(null=True, blank=True, upload_to="posts/images/")
    likes = models.ManyToManyField(UserCustom, related_name = "post_likes")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


