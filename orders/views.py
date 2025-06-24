from django.shortcuts import render
from django.contrib import messages


def design_order(request):
    return render(request, 'design_order.html'),
