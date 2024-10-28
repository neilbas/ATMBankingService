from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BankAccount

class DepositForm(forms.Form):
    account_number = forms.CharField(max_length=20)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)

class WithdrawForm(forms.Form):
    account_number = forms.CharField(max_length=20)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)

class SendMoneyForm(forms.Form):
    sender_account_number = forms.CharField(max_length=20)
    recipient_account_number = forms.CharField(max_length=20)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)

class ChangePinForm(forms.Form):
    account_number = forms.CharField(max_length=20)
    old_pin = forms.CharField(max_length=4, widget=forms.PasswordInput)
    new_pin = forms.CharField(max_length=4, widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
