from django.shortcuts import render

from django.shortcuts import HttpResponse
from .models import Blog
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
page_count = 15


def home(request, *arg, **kwargs):
	req_data = request.GET
	page = int(req_data.get('page')) if 'page' in req_data else 1

	start = (page-1)*page_count
	end = page_count*page

	blogs = Blog.objects.all()[start:end]
	context={
	"blogs":blogs
	}

	template = loader.get_template('home.html')
	return HttpResponse(template.render(context, request))

def post(request, *arg, **kwargs):
	page = ""
	template = loader.get_template('write.html')
	if request.method == "POST":
		req_data = request.POST
		try:
			blog = Blog(title= req_data["title"], body= req_data["body"])
			blog.save()

			context = {
				"msg":"succussfully posted"
			}
			return HttpResponse(template.render(context,request))

		except Exception as e:
			
			context = {
				"msg":"{} occured while posting".format(str(e))
			}
			return HttpResponse(template.render(context,request))

	else:
		context = dict()
		return HttpResponse(template.render(context,request))