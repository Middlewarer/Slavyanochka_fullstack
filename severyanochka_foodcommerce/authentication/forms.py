from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-reg-class'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-reg-class'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-reg-class'}),
            'email': forms.EmailInput(attrs={'class': 'input-reg-class'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords aren't the same")

        return cd['password']
