from django.conf.urls import url
 
from dog import views
 
 
 
 
urlpatterns = [
     url(r'^$', views.dog, name='dog'),
]