from django.shortcuts import render
from django.contrib import messages
from .forms import DesignOrderForm


def design_order(request):
    if request.method == 'POST':
        form = DesignOrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your design order har been submitted. We will get back to you shortly.')
            return redirect('portfolio')
    else:
        form = DesignOrderForm()
    return render(request, 'design_order.html', {'form': form})
