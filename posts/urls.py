from django.urls import path
from . import views

urlpatterns = [
    path('', views.app_list, name="posts_list"),
    path('add', views.add, name="add"),
    path('details/<int:id>', views.details, name="details"),
]
