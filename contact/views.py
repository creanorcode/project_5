from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactMessageForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            print("FORM IS VALID. Cleaned data:")
            print(form.cleaned_data)
            contact_message = form.save()
            print("CONTACT MESSAGE SAVED:")
            print(contact_message)
            messages.success(request, "Thank you for your message! We will get back to you soon.")
            return redirect('contact:contact')
        else:
            print("FORM IS INVALID. Errors:")
            print(form.errors)
    else:
        form = ContactMessageForm()
    return render(request, 'contact/contact.html', {'form': form})
