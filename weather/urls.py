from django.urls import path
from .views import home  # Import the home view function

urlpatterns = [
    path('', home, name='home'),  # Calls the `home` function when visiting the homepage
]

