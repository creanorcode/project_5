from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'orders'

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('checkout/', views.checkout, name='checkout'),
    path('complete/<int:order_id>/', views.order_complete, name='order_complete'),
    path('history/', views.order_history, name='order_history'),
    path('detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('design/', views.design_order_view, name='design_order'),
]
