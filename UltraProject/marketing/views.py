from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import LeadOptInForm
from .models import Lead, LeadLabel


# Create your views here.
def index(request):
    return render(request, "marketing/base.html")


def lead_optin(request, lead_label):
    label = LeadLabel.objects.get(name=lead_label)
    print(label.associated_image)
    if not label:
        return Http404()

    if request.method == "POST":
        lead = Lead(
            fname=request.POST.get("fname"),
            email=request.POST.get("email"),
            label=label,
        )
        lead.save()
        return HttpResponseRedirect(f"/mkt/obrigado/{lead_label}")

    return render(request, "marketing/optin.html", {"associated_image_filename": str(label.associated_image)})


def thank_you(request, lead_label):
    label = LeadLabel.objects.get(name=lead_label)
    if not label:
        return Http404()

    return render(request, "marketing/ty_page.html")