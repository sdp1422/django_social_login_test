from django.db import models

# 이미지 키트 import
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Blog(models.Model):
    text = models.TextField()

# 썸네일 모델 하기 위해 추가
class Pictures(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to="blogimg")
    
    # image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(120, 60)])
    
    # 속성 추가하고 싶을 때 - JPEG 형식, 압축 방식 : 60
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(200, 100)], format='JPEG', options={'quality':60})
