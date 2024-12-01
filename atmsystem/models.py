from django.db import models
from django.core.exceptions import ValidationError

class BankAccount(models.Model):
    account_number = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    pin = models.CharField(max_length=4)  # Assuming pin is a 4-digit string

    def deposit(self, amount):
        if amount <= 0:
            raise ValidationError("Deposit amount must be positive.")
        self.balance += amount
        self.save()
        Deposit.objects.create(account=self, amount=amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValidationError("Withdrawal amount must be positive.")
        if self.balance < amount:
            raise ValidationError("Insufficient balance.")
        self.balance -= amount
        self.save()
        Withdrawal.objects.create(account=self, amount=amount)

    def send_money(self, recipient_account_number, amount):
        recipient = BankAccount.objects.get(account_number=recipient_account_number)
        if self.balance < amount:
            raise ValidationError("Insufficient funds for transfer.")
        self.balance -= amount
        recipient.balance += amount
        self.save()
        recipient.save()
        Transfer.objects.create(sender=self, recipient=recipient, amount=amount)

    def change_pin(self, old_pin, new_pin):
        if self.pin != old_pin:
            raise ValidationError("Old PIN does not match.")
        self.pin = new_pin
        self.save()

class Transaction(models.Model):
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

class Deposit(Transaction):
    pass

class Withdrawal(Transaction):
    pass

class Transfer(models.Model):
    sender = models.ForeignKey(BankAccount, related_name='sent_transfers', on_delete=models.CASCADE)
    recipient = models.ForeignKey(BankAccount, related_name='received_transfers', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)