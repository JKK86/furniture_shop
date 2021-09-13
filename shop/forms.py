import django.forms as forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from shop.models import CustomizedProduct


class CustomizedProductForm(ModelForm):
    class Meta:
        model = CustomizedProduct
        exclude = ['slug', 'price', 'created', 'updated', 'status', 'user']
