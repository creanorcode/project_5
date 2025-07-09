from django.urls import path
from . import views
from .views import new_message_view, contact_thread_view, thread_list_view


app_name = 'contact'


urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('my-messages/', views.user_messages_view, name='user_messages'),
    path('messages/<int:message_id>/', views.contact_detail_view, name='message_detail'),
    path('messages/new/', new_message_view, name='new_message'),
    path('thread/<int:message_id>/', contact_thread_view, name='contact_thread'),
    path('messages/new/', views.create_thread_view, name='create_thread'),
    path('threads/', thread_list_view, name='thread_list'),
]
