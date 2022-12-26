from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UserList.as_view(), name="api-users"),
    path('users/<int:pk>/', views.UserDetall.as_view(), name="api-user"),
    path('posts/', views.PostList.as_view(), name="api-posts"),
    path('posts/<int:pk>/', views.PostDetall.as_view(), name="api-post"),
]
