from django import forms
from .models import *


class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "owner", "product_image"]

    