from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()

class Comment(models.Model):
    article = models.ForeignKey("article", on_delete=models.CASCADE)
    content = models.CharField(max_length=80)