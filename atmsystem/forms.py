from django import forms
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
