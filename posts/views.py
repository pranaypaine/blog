from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect


from .forms import PostForm
# Create your views here.
from .models import Post

def post_create(request):
	#create a post
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Added post")
		return HttpResponseRedirect(instance.get_absolute_url())


	context = {
		"form": form,
	}
	return render(request, "form.html", context)

def post_detail(request, id=None):
	#detals of single post passed with id
	instance = get_object_or_404(Post, id=id)
	context = {
		"instance" : instance
	}
	return render(request, "view_detail.html", context)

def post_list(request):
	#list all the posts in the app
	post_data = Post.objects.all().order_by("-dateadded")
	paginator = Paginator(post_data, 10) # Show 25 contacts per page
	page_req_var = 'page'
	page = request.GET.get(page_req_var)
	try:
		data = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		data = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		data = paginator.page(paginator.num_pages)

	context = {
		"title" : "post list",
		"data" : data
	}
	return render(request, "post_list.html", context)

""" 
render function takes the request and returns it to a template with the data in tuple
"""

def post_update(request, id=None):
	#edit post request
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully edited post")
		return HttpResponseRedirect(instance.get_absolute_url())


	
	context = {
		"title": instance.title,
		"instance" : instance,
		"form": form,
	}
	return render(request, "form.html", context)


def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	#delete post
	return redirect("list")