from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Lead, LeadLabel
from django.contrib.auth.decorators import user_passes_test
from .forms import EmailCampaignForm


# Create your views here.
def index(request):
    return HttpResponseRedirect("/")


def lead_optin(request, lead_label):
    label = LeadLabel.objects.get(name=lead_label)
    print(LeadLabel.objects.all())
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


@user_passes_test(lambda u: u.is_superuser)
def email_campaign(request):
    form = EmailCampaignForm()
    if request.method == "POST":
        if form.is_valid():
            pass

    return render(request, "marketing/email_campaign.html", {"form": form})