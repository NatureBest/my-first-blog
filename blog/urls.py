from django.conf.urls import *
from blog.views import archive
from django.contrib import admin
from . import search,search2
admin.autodiscover()

urlpatterns = [
              url(r'^$',archive),
              url(r'^search-form$', search.search_form),
              url(r'^search$', search.search),
              url(r'^search-post$', search2.search_post),
              ]