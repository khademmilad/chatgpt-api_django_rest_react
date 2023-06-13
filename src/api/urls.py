from django.urls import path
from .views import save_form_data

urlpatterns = [
    path("save-form/", save_form_data, name="save_form_data"),
    # Add more FastAPI URL patterns if needed
]
