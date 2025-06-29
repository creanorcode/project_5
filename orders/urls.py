from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='design_order.html'), name='design_order'),
    path('', views.order_list, name='order_list'),
    path('checkout/', views.checkout, name='checkout'),
]
