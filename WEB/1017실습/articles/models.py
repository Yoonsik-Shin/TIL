from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    image = models.ImageField(
        blank=True, 
        upload_to='image/'
    )
    thumbnail = ProcessedImageField(
        blank=True, 
        processors=[Thumbnail(200, 300)], 
        format='JPEG', 
        options={'quality': 90},
    )