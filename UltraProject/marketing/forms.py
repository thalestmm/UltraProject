from django import forms
from .models import Lead, LeadLabel


class EmailCampaignForm(forms.Form):
    recipient_label = forms.ModelChoiceField(queryset=LeadLabel.objects)
    message = forms.CharField(widget=forms.Textarea, max_length=600)