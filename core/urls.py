from django.urls import path

from core import views

urlpatterns = [
    path("", views.index, name="home"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path('getemail/',views.get_email,name='getemail'),
    
]
