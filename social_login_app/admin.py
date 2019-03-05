from django.contrib import admin
from .models import Blog
from .models import Pictures # 미디어 파일 등록 위해 import

# Register your models here.
admin.site.register(Blog)

# 미디어 파일 등록 위해
admin.site.register(Pictures)