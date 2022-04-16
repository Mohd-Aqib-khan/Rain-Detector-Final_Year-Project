from django.urls import path
from MachineLearning import views

urlpatterns = [
    path('statecmp/', views.stateComparsion, name='statecmp'),
    path('stateview/<int:sid>/', views.state_view, name='stateview'),
    
]
