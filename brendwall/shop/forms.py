from django import forms
from django.db.models import DecimalField

from shop.models import Product


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': "Например: Плов",
                'type': "text",
                'id': "name",
                'name': "title"
            }),
            'description': forms.Textarea(attrs={
                'placeholder': "Например: Берём сначала укропу...",
                'id': "description",
                'name': "description",
                'cols': 60,
                'rows': 10,
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': "Например: 777.77",
                'type': "number",
                'id': "price",
                'name': "price",
                'step': "0.01",
            }),
        }
