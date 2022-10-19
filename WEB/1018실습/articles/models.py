from email.policy import default
from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):
    article = models.ForeignKey("article", on_delete=models.CASCADE)
    content = models.CharField(max_length=80)