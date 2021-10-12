from django.shortcuts import render

from django.shortcuts import HttpResponse
from .models import Blog
from django.views.decorators.csrf import csrf_exempt

page_count = 15

default_page = '''
			<br>
			<nav margin>
				&nbsp &nbsp &nbsp
			  	
			  	<a href="/blog/"> <b> Homepage </b> </a> 

			  	&nbsp &nbsp | &nbsp &nbsp
				
				<a href="/blog/post/"> <b> Post </b> </a>
			</nav>
			<hr> 
			'''

def home(request, *arg, **kwargs):
	req_data = request.GET
	page = int(req_data.get('page')) if 'page' in req_data else 1

	start = (page-1)*page_count
	end = page_count*page

	blogs = Blog.objects.all()[start:end]
	page = default_page
	page += '''
		<h2>Blogs</h2><hr>
	'''

	if bool(blogs):
		for blog in blogs:
			page  += "<h4>"+ str(blog.title)+"</h4>"
			page  += "<p>"+ str(blog.body)+"</p>"
			page  += "<hr>"
	else:
		page+='''
			<center><h3>Nothing on this page</h3><center>

		'''

	return HttpResponse(page)

@csrf_exempt
def post(request, *arg, **kwargs):
	page = default_page
	if request.method == "POST":
		req_data = request.POST
		data_list = ["title", "body"]
		for data in data_list:
			if not data in req_data:
				page +='''
				<center>
					<h2>{} not sent</h2>
				</center>
				'''.format(data)
				return HttpResponse(page)
		try:
			blog = Blog(title= req_data["title"], body= req_data["body"])
			blog.save()
			page+='''
				<center>
					<h2>saved successfully</h2>
				</center>
				'''
			return HttpResponse(page)

		except Exception as e:
			page+='''
				<center>
					<h2>could not post due to {}</h2>
				</center>
				'''.format(str(e))
			return HttpResponse(page)

	else:
		
		page+='''
			<center>
				<h2>Your thoughts..</h2>
				<form method= "post" action="/blog/post/">
					<textarea name= "title" rows="2" cols="50" placeholder="Title of you post" required></textarea><br>
					<br>
					<textarea name= "body" rows="10" cols="50" placeholder="Write your thought here"  required></textarea><br><br>
					<button type = "submit">Post</buttom> 
					</form>
			</center>
			'''
		return HttpResponse(page)
