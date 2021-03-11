import django.forms as forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(label="Ilość", min_value=1, max_value=10, initial=1)
    override_quantity = forms.BooleanField(initial=False, required=False, widget=forms.HiddenInput)
