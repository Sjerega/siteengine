from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def test_page(request):
    return render(request, 'test_page.html')
