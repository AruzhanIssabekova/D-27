from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='home'),
    path('create/', views.create_task_with_comments, name='create'),
    path('success/', views.success, name='success'),
]

