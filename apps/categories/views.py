from django.http import HttpRequest
from django.shortcuts import render, redirect
from .forms import CategoryForm
from .models import Category

def add_category(request: HttpRequest):
    template_name = 'categories/add_category.html'
    context = {}

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('categories:list_categories')
        
    form = CategoryForm()
    context['form'] = form
    return render(request, template_name, context)

def list_categories(request: HttpRequest):
    template_name = 'categories/list_categories.html'
    categories = Category.objects.filter() #all() ?
    context = {
        'categories': categories
    }
    return render(request, template_name, context)