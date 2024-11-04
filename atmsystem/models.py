from django.db import models
from django.core.exceptions import ValidationError


class BankAccount(models.Model):
    account_number = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def deposit(self, amount):
        if amount <= 0:
            raise ValidationError("Deposit amount must be positive.")
        self.balance += amount
        self.save()

    def withdraw(self, amount):
        if amount <= 0:
            raise ValidationError("Withdrawal amount must be positive.")
        if self.balance < amount:
            raise ValidationError("Insufficient balance.")
        self.balance -= amount
        self.save()

    def send_money(self, recipient_account_number, amount):
        recipient = BankAccount.objects.get(account_number=recipient_account_number)
        if self.balance < amount:
            raise ValidationError("Insufficient funds for transfer.")
        self.balance -= amount
        recipient.balance += amount
        self.save()
        recipient.save()

    def change_pin(self, old_pin, new_pin):
        # Assuming `pin` is an attribute on the model
        if self.pin != old_pin:
            raise ValidationError("Old PIN does not match.")
        self.pin = new_pin
        self.save()

