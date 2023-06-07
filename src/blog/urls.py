from django.urls import path
from .views import post_form_view

urlpatterns = [
    path('post-form/', post_form_view, name='post_form'),
]
