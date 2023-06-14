# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('posts/user/<int:user_id>/', views.UserPostListAPIView.as_view(), name='user-post-list'),
]
