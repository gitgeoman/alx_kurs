from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="posts_list"),
    path('add', views.add, name="add"),
    path('details/<int:id>', views.details, name="details"),
]
