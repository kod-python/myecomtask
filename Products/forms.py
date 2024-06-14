from django import forms



class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='First Name*')
    last_name = forms.CharField(max_length=50, label='Last Name*')
    company_name = forms.CharField(max_length=100, required=False, label='Company Name')
    address = forms.CharField(widget=forms.Textarea, label='Address *')
    house_number_street_name = forms.CharField(max_length=100, label='House Number Street Name')
    town_city = forms.CharField(max_length=50, label='Town/City*')
    country = forms.CharField(max_length=50, label='Country*')
    postcode_zip = forms.CharField(max_length=20, label='Postcode/Zip*')
    mobile = forms.CharField(max_length=20, label='Mobile*')
    email_address = forms.EmailField(label='Email Address*')
   
    create_account = forms.BooleanField(required=False, label='Create an account?')
    ship_to_different_address = forms.BooleanField(required=False, label='Ship to a different address?')

    PAYMENT_CHOICES = [
        ('direct_bank_transfer', 'Direct Bank Transfer'),
        ('check_payments', 'Check Payments'),
        ('cash_on_delivery', 'Cash On Delivery'),
        ('paypal', 'Paypal'),
    ]

    payment_method = forms.MultipleChoiceField(
        choices=PAYMENT_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='Payment Method'
    )










# class CheckoutForm(forms.Form):
#       first_name = forms.CharField(max_length=50, label='First Name*')
#       last_name = forms.CharField(max_length=50, label='Last Name*')
#       email = forms.CharField(label='Email*')
#       mobile = forms.CharField(max_length=50, label='Mobile*')
#       shipping = forms.CharField(max_length=50, label='shipping*')
      

# class CheckoutForm(forms.Form):
#     shipping_address = forms.CharField(widget=forms.Textarea)
#     billing_address = forms.CharField(widget=forms.Textarea)
#     payment_method = forms.ChoiceField(choices=[('card', 'Credit/Debit Card'), ('paypal', 'PayPal')])















# class CheckoutForm(forms.Form):
#     shipping_address = forms.CharField(widget=forms.Textarea)
#     billing_address = forms.CharField(widget=forms.Textarea)
#     payment_method = forms.ChoiceField(choices=[('card', 'Credit/Debit Card'), ('paypal', 'PayPal')])
