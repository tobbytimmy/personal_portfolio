from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.all().order_by('-date')[:5]
    return render(request, "blog/all_blogs.html", {"Blogs": blogs})