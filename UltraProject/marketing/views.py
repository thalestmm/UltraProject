from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Lead, LeadLabel, UnsubscribeEvent
from django.contrib.auth.decorators import user_passes_test
from .forms import EmailCampaignForm, UnsubscribeForm, LeadExamForm

from django.core.exceptions import ValidationError, ObjectDoesNotExist


# Create your views here.
def index(request):
    return HttpResponseRedirect("/")


def lead_optin(request, lead_label):
    try:
        label = LeadLabel.objects.get(name=lead_label)
    except ObjectDoesNotExist:
        raise Http404()

    form = LeadExamForm()

    if request.method == "POST":
        print(request.POST)
        form = LeadExamForm(request.POST)

        if form.is_valid():
            lead = Lead(
                fname=request.POST['fname'],
                email=request.POST['email'],
                exam=form.cleaned_data['exam'],
                label=label,
            )
            lead.save()

        return HttpResponseRedirect(f"/mkt/obrigado/{lead_label}")

    return render(request, "marketing/optin.html", {"form": form, "associated_image_filename": str(label.associated_image)})


def thank_you(request, lead_label):
    try:
        label = LeadLabel.objects.get(name=lead_label)
    except ObjectDoesNotExist:
        raise Http404()

    return render(request, "marketing/ty_page.html")


def unsubscribe_from_mailing_list(request, user_uuid):
    try:
        user = Lead.objects.get(uuid=user_uuid)
    except ValidationError:
        raise Http404()

    user_email = user.email

    form = UnsubscribeForm()

    if request.method == "POST":
        form = UnsubscribeForm(request.POST)

        if "abort" in request.POST:
            pass
        if "unsubscribe" in request.POST:
            target = Lead.objects.filter(email=user_email)

            for lead in target:
                lead.email_mkt = False
                lead.save()

            if form.is_valid():
                reason = form.cleaned_data['reason']

                event = UnsubscribeEvent(reason=reason)
                event.save()

        return HttpResponseRedirect("/")

    return render(request, "marketing/unsubscribe.html", {"fname": user.fname, "form": form})


# TODO: ADD FUNCTIONALITY TO SEND EMAIL TO ALL REGISTERED LEADS (THAT HAVE EMAIL_MKT == TRUE)
@user_passes_test(lambda u: u.is_superuser)
def email_campaign(request):
    form = EmailCampaignForm()
    if request.method == "POST":
        form = EmailCampaignForm(request.POST)

        if form.is_valid():
            # SEND EMAIL -> INCLUDING LEAD DATA FOR CUSTOM EMAILS
            pass

        return HttpResponseRedirect("/mkt/email-campaign")

    return render(request, "marketing/email_campaign.html", {"form": form})
