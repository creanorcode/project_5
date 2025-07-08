from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import (
    my_completed_designs,
    create_checkout_session,
    PaymentSuccessView,
    PaymentCancelledView,
)

app_name = 'orders'

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('checkout/', views.checkout, name='checkout'),
    path('complete/<int:order_id>/', views.order_complete, name='order_complete'),
    path('history/', views.order_history, name='order_history'),
    path('detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('design/', views.design_order_view, name='design_order'),
    path('complete/success/', views.order_success, name='order_success'),
    path('webhook/', views.stripe_webhook, name='stripe_webhook'),
    path('completed-designs/', views.my_completed_designs, name='completed_designs'),
    path('pay/<int:design_id>/', views.pay_for_design, name='pay_for_design'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('checkout/<int:design_id>/', views.stripe_checkout, name='stripe_checkout'),
    path('completed-designs/', my_completed_designs, name='completed_designs'),
    path('create-checkout-session/<int:design_id>/', create_checkout_session, name='create_checkout_session'),
    path('payment/success/', PaymentSuccessView.as_view(), name='payment_success'),
    path('payment/cancelled/', PaymentCancelledView.as_view(), name='payment_cancelled'),
]
