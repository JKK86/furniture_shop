import django.forms as forms

from shop.models import CustomizedProduct


class CustomizedProductForm(forms.ModelForm):
    class Meta:
        model = CustomizedProduct
        exclude = ['slug', 'price', 'created', 'updated', 'status', 'user', 'date']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 7}),
            'file': forms.FileInput(attrs={'accept': 'application/pdf, image/jpeg'})
        }
