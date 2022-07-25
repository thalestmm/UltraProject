from django import forms
from .models import Lead, LeadLabel, UnsubscribeReason


class EmailCampaignForm(forms.Form):
    recipient_label = forms.ModelChoiceField(queryset=LeadLabel.objects)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea, max_length=600)


class UnsubscribeForm(forms.Form):
    reason = forms.ModelChoiceField(queryset=UnsubscribeReason.objects, label="Motivo")
