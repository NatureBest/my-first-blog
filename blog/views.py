# -*- coding: UTF-8 -*-
# from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from blog.models import BlogsPost
from django.shortcuts import render_to_response,get_object_or_404,render,redirect
from .forms import PostForm
from datetime import *

#from . import  search
#Create your views here.
#def archive(request):
#    posts = BlogsPost.objects.all()
#    t = loader.get_template("archive.html")
#    c = Context({'posts':posts})
#    return HttpResponse(t.render(c))
def archive(request):
    blog_list=BlogsPost.objects.all()
    return render_to_response('blog/archive.html',{'blog_list':blog_list})

def post_detail(request, pk):
    #global blog_list
    blog_list = get_object_or_404(BlogsPost, pk=pk)
    return render(request, 'blog/post_detail.html', {'blog_list': blog_list})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.tiemstamp = datetime.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(BlogsPost, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = datetime.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})