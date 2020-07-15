from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from django.conf.urls.static import static

# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})
