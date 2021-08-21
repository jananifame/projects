from django.shortcuts import render
from .models import Blog
# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    render(request,'blogs\all_blogs.html',{'blogs':blogs})
