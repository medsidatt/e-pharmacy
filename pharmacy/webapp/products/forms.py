from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control select'}),
        required=False
    )

    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'quantity', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name', 'multiple': True}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
        }

