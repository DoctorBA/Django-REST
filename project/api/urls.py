from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UserList.as_view(), name="api-users"),
    path('users/<int:pk>/', views.UserDetall.as_view(), name="api-user"),
    path('posts/', views.PostList.as_view(), name="api-posts"),
    path('posts/<int:pk>/', views.PostDetall.as_view(), name="api-post"),
    path('books/', views.BookList.as_view(), name="api-books"),
    path('books/<int:pk>/', views.BookDetall.as_view(), name="api-book"),
    path('authors/', views.AuthorList.as_view(), name="api-authors"),
    path('authors/<int:pk>/', views.AuthorDetall.as_view(), name="api-author"),
]
