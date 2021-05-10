from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('createToDo/', views.createTodo, name = 'createTodo'),
    path('deleteToDo/', views.deleteTodo, name = 'deleteTodo'),
]