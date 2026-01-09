from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.contrib import messages
# Create your views here
def product(request,pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'product.html', {'product': product})

def category(request, pk):
    try:
        category = Category.objects.get(name=pk)
        products = Product.objects.filter(category=category)
        return render(request, '', {'products': products, 'category': pk})
    except:
        messages.success(request, "No products found in this category.")
        return redirect('accounts:home')
    return render(request, 'category.html', {'products': products, 'category': pk})