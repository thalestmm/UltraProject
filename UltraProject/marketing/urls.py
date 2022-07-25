from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.index, name="index"),
    path("optin/<str:lead_label>", views.lead_optin, name="optin"),
    path("obrigado/<str:lead_label>", views.thank_you, name="ty_page"),
    path("email-campaign", views.email_campaign, name="email_campaign"),
    path("unsubscribe/<str:user_uuid>", views.unsubscribe_from_mailing_list, name="unsubscribe")
]

urlpatterns += staticfiles_urlpatterns()
