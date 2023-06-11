from django.urls import path
from .views import profile

app_name = 'account'

urlpatterns = [
    # Other URL patterns
    path('profile/<str:username>/', profile, name='profile'),
]