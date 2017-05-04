# -*- coding: UTF-8 -*-
# from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from blog.models import BlogsPost
from django.shortcuts import render_to_response
from . import  search
#Create your views here.
#def archive(request):
#    posts = BlogsPost.objects.all()
#    t = loader.get_template("archive.html")
#    c = Context({'posts':posts})
#    return HttpResponse(t.render(c))
def archive(request):
    blog_list=BlogsPost.objects.all()
    return render_to_response('archive.html',{'blog_list':blog_list})