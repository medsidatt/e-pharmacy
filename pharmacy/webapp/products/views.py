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


from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ProductForm


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data['category']
            category, created = Category.objects.get_or_create(name=category_name)  # Create if not exists

            product = form.save(commit=False)
            product.category = category  # Assign category to product
            product.save()
            return redirect('product_list')  # Redirect after saving
    else:
        form = ProductForm()

    return render(request, 'products/create.html', {'form': form})
