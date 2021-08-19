from django import forms
from .models import *

class AddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['received_quantity']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ["quantity", "amount_received", "issued_to"]
