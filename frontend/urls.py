from django.urls import path
from frontend import views

# route url
urlpatterns = [
    path("", views.home, name="home")
]