from django import forms
from django.forms import ModelForm
from .models import Post, User_login


class PostForm(forms.ModelForm):
	"""docstring for PostForm"""
	class Meta:
		model = Post
		fields = [
			"title",
			"image",
			"content",
		]

class UserForm(forms.ModelForm):
	"""docstring for UserForm"""
	class Meta:
		model = User_login
		fields = [
			"username",
			"password"
		]
		