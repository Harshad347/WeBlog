from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Comment(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, null=True)
    commentator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField(max_length=200, null=True)
    commented_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.commentator} | {self.body}'

    class Meta:
        ordering = ['-commented_on']

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.Post.pk})
