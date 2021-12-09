from django.shortcuts import render

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
        'h1': 'Store Products h1'
    }
    return render(request, 'products\products.html', context)


def test(request):
    context = {
        'title': 'Страница экспериментов',
        'h1': 'Test h1'
    }
    return render(request, 'test.html', context)
