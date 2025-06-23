from django.urls import path
from . import views

urlpatterns = [
    path('design/', views.design_order, name='design_order'),
]
