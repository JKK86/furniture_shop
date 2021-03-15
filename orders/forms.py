import django.forms as forms

from orders.models import DELIVERY_TYPES, DeliveryAddress
from orders.validators import validate_postal_code


class DeliveryTypeForm(forms.Form):
    delivery_type = forms.ChoiceField(choices=DELIVERY_TYPES, label="Sposób dostawy", widget=forms.RadioSelect)


class DeliveryAddressForm(forms.Form):
    address = forms.CharField(max_length=255, label='Adres')
    postal_code = forms.CharField(max_length=6, label='Kod pocztowy', validators=[validate_postal_code])
    city = forms.CharField(max_length=64, label="Miasto")
