from django.http import request
from django.shortcuts import render
from django.views import generic
from .models import Post, Project, Connect

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blogs.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def index(request):
    return render(request, 'index.html')

def projects(request):
    project = Project.objects.all()
    return render(request,'projects.html', {'projects': project})

def connect(request):
    connect = Connect.objects.all()
    return render(request,'connect.html', {'connect': connect})
