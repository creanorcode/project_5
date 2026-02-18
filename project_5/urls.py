"""
URL configuration for project_5.

Routes core pages, app URLs, and SEO endpoints (robots.txt + sitemap.xml)
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.generic import TemplateView

from accounts.views import newsletter_view
from core.sitemaps import sitemaps
from core.views import robots_txt

urlpatterns = [
    path('admin/', admin.site.urls),

    # Static pages
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('portfolio/', TemplateView.as_view(template_name='portfolio.html'), name='portfolio'),

    # Apps
    path('accounts/', include('accounts.urls')),
    path('', include('portfolio.urls')),
    path('products/', include('products.urls')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),

    # SEO
    path('robots.txt', robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap_xml'),

    # Marketing
    path('newsletter/', newsletter_view, name='newsletter'),
]

handler404 = 'accounts.views.custom_404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
