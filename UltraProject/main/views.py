from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(response):
    return HttpResponse("WORKING")


def home(response):
    return render(response, "main/home.html")


def terms_of_use(response):
    return render(response, "main/terms.html")


def privacy_policy(response):
    return render(response, "main/privacy_policy.html")