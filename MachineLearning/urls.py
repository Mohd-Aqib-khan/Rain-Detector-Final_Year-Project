from django.urls import path
from MachineLearning import views

urlpatterns = [
    path('statecmp/', views.stateComparsion, name='statecmp'),
    path('rainprediction/', views.rainPredication, name='rainpred'),
    path('stateview/<int:sid>/', views.state_view, name='stateview'),    
]
