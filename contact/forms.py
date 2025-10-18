# contact/forms.py
from django import forms

from .models import ContactMessage, Message, MessageThread, ThreadMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'Your email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Your message', 'rows': 5
            }),
        }


class UserReplyForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['user_reply']
        widgets = {
            'user_reply': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your message here...',
            })
        }


class NewMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Write your message here...',
                'class': 'form-control'
            }),
        }
        labels = {
            'content': ''
        }


class NewThreadForm(forms.ModelForm):
    class Meta:
        model = MessageThread
        fields = ['subject']


class FirstMessageForm(forms.ModelForm):
    class Meta:
        model = ThreadMessage
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 5}),
        }
