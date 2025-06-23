from django.shortcuts import render


def home(request):
    return render(request, 'portfolio/home.html')


def portfolio(request):
    return render(request, 'portfolio.html')
