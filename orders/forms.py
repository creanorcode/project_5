from django import forms

from .models import DesignOrder, DesignType


class DesignOrderForm(forms.ModelForm):
    class Meta:
        model = DesignOrder
        fields = ['name', 'email', 'description', 'design_type', 'attachment']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe your design needs',
                'rows': 5
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = DesignType.objects.all()
        if choices.exists():
            description_list = [f"<strong>{dt.name}</strong>: {dt.description}" for dt in choices]
            self.fields['design_type'].help_text = "<br>".join(description_list)


class CheckoutForm(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        label="Full name",
        widget=forms.TextInput(attrs={"placeholder": "Your full name"})
    )
    email = forms.EmailField(
        label="Email address",
        widget=forms.EmailInput(attrs={"placeholder": "you@example.com"})
    )
    address = forms.CharField(
        max_length=250,
        label="Street address",
        widget=forms.TextInput(attrs={"placeholder": "123 Main Street"})
    )
    postal_code = forms.CharField(
        max_length=20,
        label="Postal code",
        widget=forms.TextInput(attrs={"placeholder": "12345"})
    )
    city = forms.CharField(
        max_length=100,
        label="City",
        widget=forms.TextInput(attrs={"placeholder": "Stockholm"})
    )
    country = forms.CharField(
        max_length=100,
        label="Country",
        initial="Sweden"
    )
    instructions = forms.CharField(
        required=False,
        label="Design instructions (optional)",
        widget=forms.Textarea(attrs={"placeholder": "If you have any design preferences, enter them here."})
    )
