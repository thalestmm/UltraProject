from django import forms


class LeadOptIn(forms.Form):
    fname = forms.CharField(name="fname", max_length=20)
    email = forms.EmailField(name="email")