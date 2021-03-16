import django.forms as forms
from cart.models import COLORS, NATURALNY


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(label="Ilość", min_value=1, max_value=10, initial=1)
    override_quantity = forms.BooleanField(initial=False, required=False, widget=forms.HiddenInput)


class CartSetColorForm(forms.Form):
    color = forms.ChoiceField(label="Kolor", choices=COLORS, initial=NATURALNY, widget=forms.RadioSelect)
