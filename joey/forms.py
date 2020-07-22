from django import forms
from jsignature.forms import JSignatureField
from django.utils.translation import gettext_lazy as _

class SignatureForm(forms.Form):
    signature = JSignatureField()

class ConsultationForm(forms.Form):
    client = forms.CharField()
    signature = JSignatureField()

