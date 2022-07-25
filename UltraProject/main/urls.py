from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.home, name="index"),
    path("terms-of-use", views.terms_of_use, name="terms"),
    path("privacy-policy", views.privacy_policy, name="privacy_policy"),
]

urlpatterns += staticfiles_urlpatterns()
