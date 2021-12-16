from django.shortcuts import render
from products.models import ProductCategory, Product

# Create your views here.


def index(request):
    context = {
        'title': 'Магазин молодежной одежды',
        'h1': 'Store h1',
    }
    return render(request, 'products\index.html', context)


def products(request):
    context = {
        'title': 'Каталог товаров',
        'h1': 'Store Products h1',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'products\products.html', context)


def test(request):
    context = {
        'title': 'Страница экспериментов',
        'h1': 'Test h1',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all()
    }
    return render(request, 'test.html', context)
