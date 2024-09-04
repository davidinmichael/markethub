from django import forms
from .models import *


class ProductAddForm(forms.Form):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "owner"]