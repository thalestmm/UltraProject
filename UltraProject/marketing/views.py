from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(response):
    return HttpResponse(200, "Working")


def lead_optin(response):
    return render(response, "marketing/optin.html")