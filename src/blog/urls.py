from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('create-post/', views.post_form_view, name='post_form'),
    
]
