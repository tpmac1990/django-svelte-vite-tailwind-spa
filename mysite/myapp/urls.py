from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.BlogsList.as_view(), name='blogs'),
    path('blogs/<int:pk>/', views.BlogIndex.as_view(), name='blog'),
]