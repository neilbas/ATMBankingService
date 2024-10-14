from django.db import models
from django.core.exceptions import ValidationError


class BankAccount(models.Model):
    account_number = models.CharField(max_length=20, unique=True)
    account_holder = models.CharField(max_length=100)
    pin = models.CharField(max_length=4)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def deposit(self, amount):
        if amount <= 0:
            raise ValidationError("Deposit amount must be greater than zero.")
        self.balance += amount
        self.save()

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValidationError("Insufficient funds.")
        self.balance -= amount
        self.save()

    def check_balance(self):
        return self.balance

    def send_money(self, recipient_account_number, amount):

        try:
            recipient = BankAccount.objects.get(account_number=recipient_account_number)
        except BankAccount.DoesNotExist:
            raise ValidationError("Recipient account does not exist.")

        if self.balance < amount:
            raise ValidationError("Insufficient funds to complete the transfer.")

        self.withdraw(amount)
        recipient.deposit(amount)

    def change_pin(self, old_pin, new_pin):

        if self.pin != old_pin:
            raise ValidationError("Old PIN is incorrect.")
        if len(new_pin) != 4:
            raise ValidationError("New PIN must be 4 digits.")
        self.pin = new_pin
        self.save()

    def __str__(self):
        return f"Account {self.account_number} - {self.account_holder}"
