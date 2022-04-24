from django.urls import path

from core import views

urlpatterns = [
    path("", views.index, name="home"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path('getemail/',views.get_email,name='getemail'),
    path('create/',views.create_account,name="create"),
    path('login/',views.user_login,name="login"),
    path('logout/', views.user_logout, name="logout"),
    
    
]
