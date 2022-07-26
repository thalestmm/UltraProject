from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(response):
    return HttpResponse("WORKING")


def home(request):
    return render(request, "main/home.html")


def pricing(request):
    return render(request, "main/pricing.html")


def terms_of_use(request):
    return render(request, "main/terms.html")


def privacy_policy(request):
    return render(request, "main/privacy_policy.html")