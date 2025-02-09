from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    category = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control select2', 'placeholder': 'Select or create a category'}),
        required=True
    )

    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'quantity', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
        }
