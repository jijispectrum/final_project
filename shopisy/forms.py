# forms.py

from django import forms
from .models import Product

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']


from django import forms
from .models import BillingDetails

from django import forms
from .models import BillingDetails

class BillingDetailsForm(forms.ModelForm):
    class Meta:
        model = BillingDetails
        fields = ['name', 'phone_number', 'email', 'address', 'postal_code', 'company_name']