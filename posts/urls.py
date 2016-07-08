from django.conf.urls import url
from django.contrib import admin

"""
	url routing for the app posts
"""
from  .views import(
	post_list,
	post_create,
	post_update,
	post_delete,
	post_detail,
	login
)

urlpatterns = [
    url(r'^$', post_list, name="list"),
    url(r'^create/$', post_create, name="add"),
    url(r'^edit/(?P<id>\d+)/$', post_update, name="edit"),
    url(r'^(?P<id>\d+)/$', post_detail, name="detail"),
    url(r'^(?P<id>\d+)/delete/$', post_delete, name="delete"),
    url(r'^login/$', login, name="login"),

]
# go through vid 19 again for url better routing