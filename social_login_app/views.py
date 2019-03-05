from django.shortcuts import render
from .models import Pictures # for media file

# Create your views here.
def home(request):
    blog = Pictures.objects ## for media file
    return render(request, 'home.html', {'blog': blog})