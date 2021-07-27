from django.urls import path
from . import views

urlpatterns = [
        path('createPerson', views.createPerson),
        path('createList', views.createList),
        path('<str:name>', views.index),
        path('', views.home),   
]
