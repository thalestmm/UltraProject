from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("terms-of-use", views.terms_of_use, name="terms"),
    path("privacy-policy", views.privacy_policy, name="privacy_policy"),
]