from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, "Thank you for your message! We´ll be in touch soon.")
            form = ContactForm()  # Empty the form
    else:
        form = ContactForm()
    return render(render, 'contact/contact.html', {'form': form})


def home(request):
    return render(request, 'portfolio/home.html')


def portfolio(request):
    return render(request, 'portfolio.html')
