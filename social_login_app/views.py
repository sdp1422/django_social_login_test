from django.shortcuts import render
from .models import Pictures # 미디어 파일 등록 위해

# Create your views here.
def home(request):
    blog = Pictures.objects ## 미디어 파일 위해
    return render(request, 'home.html', {'blog': blog})