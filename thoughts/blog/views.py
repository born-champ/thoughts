from django.shortcuts import render

from django.shortcuts import HttpResponse
from .models import Blog
from django.views.decorators.csrf import csrf_exempt

def home(request, *arg, **kwargs):
	blogs = Blog.objects.all()
	page = '''
	<a href="/blog/"> Homepage</a>
	<a href="/blog/post/"> Post</a>
	<hr>

	<h2>Blogs</h2><br>'''
	for blog in blogs:
		page  = page + "<h3>"+ str(blog.id)+"</h3>"
		page  = page + "<h4>"+ str(blog.title)+"</h4>"
		page  = page + "<p>"+ str(blog.body)+"</p>"
		page  = page + "<hr>"

	return HttpResponse(page)

@csrf_exempt
def post(request, *arg, **kwargs):
	page = '''
			<a href="/blog/"> Homepage</a>
			<a href="/blog/post/"> Post</a>
			<hr>'''
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
				<h2>Fill data here</h2>
				<form method= "post" action="/blog/post/">
					Title: <input type = "text" name="title" required/><br>
					Body: <textarea name= "body" required>
					</textarea><br>
					<button type = "submit">Post</buttom> 
					</form>
			</center>
			'''
		return HttpResponse(page)
