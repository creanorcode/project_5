from django.urls import path

from . import views
from .views import (
    PaymentCancelledView,
    ShopPaymentSuccessView,
    checkout,
    pay_for_design
)

app_name = 'orders'

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('checkout/', checkout, name='checkout'),
    path('complete/<int:order_id>/', views.order_complete, name='order_complete'),
    path('history/', views.order_history, name='order_history'),
    path('detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('design/', views.design_order_view, name='design_order'),
    path('webhook/', views.stripe_webhook, name='stripe_webhook'),
    path('completed-designs/', views.my_completed_designs, name='completed_designs'),
    path('pay/<int:design_id>/', pay_for_design, name='pay_for_design'),
    path('payment-success/', views.payment_success, name='design_payment_success'),
    # path('checkout/<int:design_id>/', views.stripe_checkout, name='stripe_checkout'),
    path('admin/designs/', views.admin_design_list, name='admin_design_list'),
    path('admin/mark-paid/<int:design_id>/', views.mark_design_as_paid, name='mark_design_as_paid'),
    path('complete/success/', views.ShopPaymentSuccessView.as_view(), name='shop_success'),
    path('complete/cancel/', PaymentCancelledView.as_view(), name='payment_cancel')
]
