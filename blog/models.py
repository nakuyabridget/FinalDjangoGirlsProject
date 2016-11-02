# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    choices = (
        ('draft', 'DRAFT'),
        ('published', 'PUBLISHED'),)

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    status = models.CharField(max_length = 10, choices = choices, default='draft')


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

