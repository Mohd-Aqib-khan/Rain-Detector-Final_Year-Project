from django.urls import path, include

from core import views

urlpatterns = [
    path("", views.index, name="home"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
]
