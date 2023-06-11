from django.urls import path
from account import views

app_name = 'account'

urlpatterns = [
    path('profile/<str:username>/', views.profile, name='profile'),
    path('delete-post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('preview-pdf/<int:post_id>/', views.preview_pdf, name='preview_pdf'),


]