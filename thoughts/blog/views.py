from django.shortcuts import render

from django.shortcuts import HttpResponse
from .models import Blog

def home(request, *arg, **kwargs):
	blogs = Blog.objects.all()
	page = "<h1>Homepage</h1><hr><h2>Blogs</h2><br>"
	for blog in blogs:
		page  = page + "<h3>"+ str(blog.id)+"</h3>"
		page  = page + "<h4>"+ str(blog.title)+"</h4>"
		page  = page + "<p>"+ str(blog.body)+"</p>"
		page  = page + "<hr>"

	return HttpResponse(page)
