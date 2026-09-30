from django import forms
from .models import Produtos

class ProductForm(forms.ModelForm):

    class Meta:
        model = Produtos
        exclude = ()