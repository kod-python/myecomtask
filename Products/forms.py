from django import forms

class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(widget=forms.Textarea)
    billing_address = forms.CharField(widget=forms.Textarea)
    payment_method = forms.ChoiceField(choices=[('card', 'Credit/Debit Card'), ('paypal', 'PayPal')])
