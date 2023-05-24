from django import forms


class PaymentForm(forms.Form):
    PAYMENT_CHOICES = (
        ('on_delivery', 'On Delivery'),
        ('bank_card', 'Bank Card'),
    )

    payment_method = forms.ChoiceField(choices=PAYMENT_CHOICES)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    delivery_address = forms.CharField(required=True)
    postal_code = forms.CharField(required=True)
    card_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'card-fields'}))
    card_expiry = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'card-fields'}))
    card_cvv = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'card-fields'}))
