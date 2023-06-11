from django.urls import path
from account import views
from django.contrib.auth import views as auth_views


app_name = 'account'

urlpatterns = [
    path('profile/<str:username>/', views.profile, name='profile'),
    path('delete-post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('preview-pdf/<int:post_id>/', views.preview_pdf, name='preview_pdf'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
]