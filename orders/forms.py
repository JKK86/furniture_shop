import django.forms as forms

from orders.models import DELIVERY_TYPES, DeliveryAddress


class DeliveryTypeForm(forms.Form):
    delivery_type = forms.ChoiceField(choices=DELIVERY_TYPES, label="Dostawa", widget=forms.RadioSelect)


class DeliveryAddressForm(forms.Form):
    address = forms.CharField(max_length=255, label='Adres')
    postal_code = forms.CharField(max_length=6, label='Kod pocztowy')
    city = forms.CharField(max_length=64, label="Miasto")
