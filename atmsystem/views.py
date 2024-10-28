from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ValidationError
from .models import BankAccount
from .forms import DepositForm, WithdrawForm, SendMoneyForm, ChangePinForm

def deposit_view(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            account = get_object_or_404(BankAccount, account_number=form.cleaned_data['account_number'])
            try:
                account.deposit(form.cleaned_data['amount'])
                return render(request, 'success.html', {'message': 'Deposit successful!'})
            except ValidationError as e:
                return render(request, 'error.html', {'message': e.message})
    else:
        form = DepositForm()
    return render(request, 'deposit.html', {'form': form})

def withdraw_view(request):
    if request.method == 'POST':
        form = WithdrawForm(request.POST)
        if form.is_valid():
            account = get_object_or_404(BankAccount, account_number=form.cleaned_data['account_number'])
            try:
                account.withdraw(form.cleaned_data['amount'])
                return render(request, 'success.html', {'message': 'Withdrawal successful!'})
            except ValidationError as e:
                return render(request, 'error.html', {'message': e.message})
    else:
        form = WithdrawForm()
    return render(request, 'withdraw.html', {'form': form})

def send_money_view(request):
    if request.method == 'POST':
        form = SendMoneyForm(request.POST)
        if form.is_valid():
            sender = get_object_or_404(BankAccount, account_number=form.cleaned_data['sender_account_number'])
            try:
                sender.send_money(form.cleaned_data['recipient_account_number'], form.cleaned_data['amount'])
                return render(request, 'success.html', {'message': 'Transfer successful!'})
            except ValidationError as e:
                return render(request, 'error.html', {'message': e.message})
    else:
        form = SendMoneyForm()
    return render(request, 'send_money.html', {'form': form})

def change_pin_view(request):
    if request.method == 'POST':
        form = ChangePinForm(request.POST)
        if form.is_valid():
            account = get_object_or_404(BankAccount, account_number=form.cleaned_data['account_number'])
            try:
                account.change_pin(form.cleaned_data['old_pin'], form.cleaned_data['new_pin'])
                return render(request, 'success.html', {'message': 'PIN change successful!'})
            except ValidationError as e:
                return render(request, 'error.html', {'message': e.message})
    else:
        form = ChangePinForm()
    return render(request, 'change_pin.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('contact')  # Redirect to a home page or dashboard
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
