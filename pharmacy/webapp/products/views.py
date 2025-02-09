from django.shortcuts import render, redirect

from webapp.products.forms import ProductForm
from webapp.products.models import Product


# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', context={
        'title': 'Product List',
        'message': 'Product List',
        'products': products,
    })

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = ProductForm()

    return render(request, 'products/create.html', {'form': form})
