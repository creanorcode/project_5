from django.urls import path
from . import views


app_name = 'contact'


urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('my-messages/', views.user_messages_view, name='user_messages'),
    path('messages/<int:message_id>/', views.contact_detail_view, name='message_detail'),
]
