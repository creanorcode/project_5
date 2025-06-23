from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')), # home and portfolio
    path('orders/', include('orders.urls')), # design order
    path('accounts/', include('accounts.urls')), # Login, Logout, register
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'), # contact
]
