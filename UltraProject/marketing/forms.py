from django import forms
from .models import Lead, LeadLabel, UnsubscribeReason

import sys
sys.path.append("..")
from main.models import Exam


class EmailCampaignForm(forms.Form):
    recipient_label = forms.ModelChoiceField(queryset=LeadLabel.objects)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea, max_length=600)


class UnsubscribeForm(forms.Form):
    reason = forms.ModelChoiceField(queryset=UnsubscribeReason.objects, label="Motivo")


class OptinForm(forms.Form):
    fname = forms.CharField(max_length=50, label="Seu primeiro nome")
    email = forms.EmailField(label="Seu melhor email")

    class Meta:
        abstract = True


class LeadOptinForm(OptinForm):
    exam = forms.ModelChoiceField(queryset=Exam.objects, label="Você está se preparando para qual prova? ")


class LeadExamForm(forms.Form):
    exam = forms.ModelChoiceField(queryset=Exam.objects, label="Você está se preparando para qual prova? ")