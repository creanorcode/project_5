from django import forms


class DesignOrderForm(forms.Form):
    # Placeholder fields
    instructions = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Any specific design instructions?'})
    )


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
