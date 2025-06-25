from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # home
    path('portfolio/', TemplateView.as_view(template_name='portfolio.html'), name='portfolio'),  # portfolio
    path('order/', TemplateView.as_view(template_name='design_order.html'), name='design_order'),  # design order
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),  # contact
    path('accounts/', include('accounts.urls')),  # djangos layout for login, logout, register
    # path('login/', TemplateView.as_view(template_name='login.html'), name='login'), login
    # path('register/', TemplateView.as_view(template_name='register.html'), name='register'), register
    path('', include('portfolio.urls')),
]
