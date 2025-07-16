from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # home
    path('portfolio/', TemplateView.as_view(template_name='portfolio.html'), name='portfolio'),  # portfolio
    # path('order/', TemplateView.as_view(template_name='design_order.html'), name='design_order'),  # design order
    # path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),  # contact
    path('accounts/', include('accounts.urls')),  # djangos layout for login, logout, register
    # path('login/', TemplateView.as_view(template_name='login.html'), name='login'), login
    # path('register/', TemplateView.as_view(template_name='register.html'), name='register'), register
    path('', include('portfolio.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('contact/', include('contact.urls', namespace='contact')),
]

handler404 = 'artea.views.custom_404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
