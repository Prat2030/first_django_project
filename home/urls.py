from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("" , views.index,name='home'),
    #  Here first what happens is that we get to the server page like 127.0.0.1:8000/ then 
    #  we write after the slash and we go to different paths where we want to go.
    #  Suppose we write 127.0.0.1:8000/about then we get to the about page.
    #  here in urls.py we mention the what to do when user goes to the path.
     
    path("about", views.about , name='about'),  
    path("services", views.services , name='services'),
    path("contact", views.contact , name='contact'),
]