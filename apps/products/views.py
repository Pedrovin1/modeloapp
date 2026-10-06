from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm

from .models import Produtos
from rest_framework import viewsets
from .serializer import ProductSerializer

# - = - = - = - = - = - MVT - = - = - = - = - = -

def add_product(request: HttpRequest):
    template_name = 'products/add_product.html'
    context = {}
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('products:list_products')
        
    form = ProductForm()
    context['form'] = form
    return render(request, template_name, context)


def list_products(request: HttpRequest):
    template_name = 'products/list_products.html'
    products = Produtos.objects.filter()
    context = {
        'products': products
    }
    return render(request, template_name, context)


def edit_product(request: HttpRequest, id_product):
    template_name = 'products/add_product.html'
    context ={}
    product = get_object_or_404(Produtos, id=id_product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES,  instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:list_products')
    form = ProductForm(instance=product)
    context['form'] = form
    return render(request, template_name, context)

def delete_product(request: HttpRequest, id_product):
    product = Produtos.objects.get(id=id_product)
    product.delete()
    return redirect('products:list_products')

# - = - = - = - = - = - REST - = - = - = - = - = -

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProductSerializer

