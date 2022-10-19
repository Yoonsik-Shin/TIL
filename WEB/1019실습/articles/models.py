from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField()

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)