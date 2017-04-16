from django.conf.urls import url
from images import views

urlpatterns = [
	url(r'^create/$', views.image_create, name='create'),
]