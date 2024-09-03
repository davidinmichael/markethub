from django import forms

from .models import Account


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["first_name", "last_name", "email", "password"]
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Account.objects.filter(email=email).exists():
            return forms.ValidationError("User Already Exist")
        return email


class ChangePasswordForm(forms.Form):
    password = forms.CharField(max_length=20)
    new_password = forms.CharField(max_length=20)
    confirm_password = forms.CharField(max_length=20)