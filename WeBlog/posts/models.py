from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True)
    cover_pic = models.ImageField(
        null=True, upload_to='media/cover_pics')
    overview = models.TextField(max_length=255)
    description = models.TextField(null=True)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)
    #slug = models.SlugField(null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    # @property
    # def author_full_name(self):
    #     try:
    #         return f'{self.author.first_name} {self.author.last_name}'
    #     except:
    #         return "Name Not Set"

    class Meta:
        ordering = ['-created_on']


@receiver(pre_save, sender=Post)
def update_updated_on(sender, instance, **kwargs):
    # Update The Date Of 'Post' When The Post Gets Updated

    if instance.id:
        old_value = Post.objects.get(pk=instance.id).updated_on
        if not old_value:
            instance.updated_on = timezone.now()
