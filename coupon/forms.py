import django.forms as forms


class AddCouponForm(forms.Form):
    code = forms.CharField(max_length=16, label="Kod")
