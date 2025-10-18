from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('portfolio/', TemplateView.as_view(template_name='portfolio.html'), name='portfolio'),
    # path('contact/', views.contact_view, name='contact'),
]
