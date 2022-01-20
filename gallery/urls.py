from django.urls import path
from .views import *


urlpatterns = [
    path('',PostListView.as_view(),name='list'),
    path('create/',PostCreateView.as_view(),name='create'),
    path('detail/<int:pk>/',PostDetailView.as_view(),name='detail'),
    path('delete/<int:pk>/',PostDeleteView.as_view(),name='delete'),
]