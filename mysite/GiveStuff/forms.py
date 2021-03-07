import django.forms as forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password_confirm = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        exclude = []

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('password_confirm')
        if password != confirm_password:
            raise forms.ValidationError('Hasła nie są takie same')





