from django.db import models

# for media file import
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Blog(models.Model):
    text = models.TextField()

# for media file
class Pictures(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to="blogimg")
    
    # image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(120, 60)])
    
    # for media file - JPEG format, compression : 60
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(200, 100)], format='JPEG', options={'quality':60})
