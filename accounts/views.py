from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Account created successfully. Welcome, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "There was a problem with your registration. Please check the form below.")
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    """
    Ska denna bort innan inlämning 
    """
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')


def logout_success(request):
    return render(request, 'accounts/logout_success.html')


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Sitemap: https://www.artea.studio/sitemap.xml"
    ]

    return HttpResponse("\n".join(lines), content_type="text/plain")
