from django.urls import path
from .views import post_form_view

app_name = 'blog'

urlpatterns = [
    path('create-post/', post_form_view, name='post_form'),
]
