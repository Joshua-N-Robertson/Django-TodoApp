from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_view, name="todo_index"),
    path('addtask/', views.addtask_view, name="todo_add"),
    path('edit/<int:pk>/', views.edit_view, name="todo_edit"),
    path('delete/<int:pk>/', views.delete_view, name="todo_delete"),
    path('close/<int:pk>/', views.close_view, name="todo_close"),
    path('clear/', views.clear_view, name="todo_clear"),
]
