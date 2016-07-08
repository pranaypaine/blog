from django.shortcuts import render

# Create your views here.

def user_login(request):
	return render(request, "login.html", {})
	pass


def user_register(request):
	return render(request, "login.html", {})
	pass

def forgot_pass(request):
	return render(request, "login.html", {})
	pass

def logout(request):
	return render(request, "login.html", {})
	pass