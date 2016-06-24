from django.contrib import admin

# Register your models here.
# importing models .models is used as model.py and admin.py are in same dir

from .models import Post

# django admin is good for cms like stuff
# for More client managed admin a seprate solution needs to be developed
# class PostModelAdmin designs the view of the django admin portal
# admin.ModelAdmin inherits from admin module
# list_display displays the headears for the posts
# search_feild creates a search bar to search content
# list_filter creates filters accrding the items in the parameter
# more info on this link https://docs.djangoproject.com/en/1.9/ref/contrib/admin/

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "dateupdated", "dateadded"]
	search_fields = ["title", "content"]
	list_filter = ["dateadded", "dateupdated", "title"]
	class meta:
		model = Post

# this line is to register the posts app to the admin
admin.site.register(Post, PostModelAdmin)