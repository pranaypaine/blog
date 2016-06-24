from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
# creates database scema in the database
# after making migrations
# models.Model extends from model module

class Post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	dateadded = models.DateTimeField(auto_now=False, auto_now_add=True)
	dateupdated = models.DateTimeField(auto_now=True, auto_now_add=False)
	
	"""docstring for Post"""
	
	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("detail", kwargs={"id": self.id})
		
		