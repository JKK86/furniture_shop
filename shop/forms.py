import django.forms as forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    password = forms.CharField(label="Hasło", min_length=8, widget=forms.PasswordInput)
    password_repeat = forms.CharField(label="Powtórz hasło", min_length=8, widget=forms.PasswordInput,
                                      help_text="Wprowadź jeszcze raz to samo hasło co powyżej")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        password_repeat = cleaned_data['password_repeat']
        if password and password_repeat and password != password_repeat:
            raise forms.ValidationError('Hasła nie są takie same')
