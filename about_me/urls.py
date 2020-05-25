from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_content, name="main_content"),
    path("about_me", views.about_me, name="about_me")
]
