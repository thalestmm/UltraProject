from django import forms


class LeadOptInForm(forms.Form):
    fname = forms.CharField(max_length=20)
    email = forms.EmailField()