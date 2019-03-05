from django.contrib import admin
from .models import Blog
from .models import Pictures # for media file import

# Register your models here.
admin.site.register(Blog)

# for media file
admin.site.register(Pictures)