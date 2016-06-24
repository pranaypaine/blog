from django import forms
from django.forms import ModelForm
from .models import Post


class PostForm(forms.ModelForm):
	"""docstring for PostForm"""
	class Meta:
		model = Post
		fields = [
			"title",
			"content"
		]