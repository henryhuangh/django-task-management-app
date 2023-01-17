from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('todo/', views.todo),
    path('add-todo/', views.create_todo),
    path('delete-todo/<int:id>', views.delete_todo)
]