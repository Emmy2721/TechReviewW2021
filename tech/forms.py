from django import forms
from  .models import TechType, Product, Review

class ProductForm(forms.ModesForm):
    class Meta:
        models=Product
        fields='__all__'