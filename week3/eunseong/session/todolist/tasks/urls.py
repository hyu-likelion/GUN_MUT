from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="list"),
    path('edit/<str:idx>', views.edit, name="edit"),
    path('delete/<str:idx>', views.delete, name="delete"),
]