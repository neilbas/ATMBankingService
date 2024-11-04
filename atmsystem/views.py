from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from .models import BankAccount
from .forms import DepositForm, WithdrawForm, SendMoneyForm, ChangePinForm, LoginForm, SignupForm

def handle_form_submission(request, form_class, success_message, template_name, action):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            account = get_object_or_404(BankAccount, account_number=form.cleaned_data['account_number'])
            try:
                action(account, form.cleaned_data)
                return render(request, 'success.html', {'message': success_message})
            except ValidationError as e:
                return render(request, 'error.html', {'message': e.message})
    else:
        form = form_class()
    return render(request, template_name, {'form': form})

def deposit_view(request):
    return handle_form_submission(
        request,
        DepositForm,
        'Deposit successful!',
        'deposit.html',
        lambda account, data: account.deposit(data['amount'])
    )

def withdraw_view(request):
    return handle_form_submission(
        request,
        WithdrawForm,
        'Withdrawal successful!',
        'withdraw.html',
        lambda account, data: account.withdraw(data['amount'])
    )

def send_money_view(request):
    def send_money_action(account, data):
        sender = account
        sender.send_money(data['recipient_account_number'], data['amount'])

    return handle_form_submission(
        request,
        SendMoneyForm,
        'Transfer successful!',
        'send_money.html',
        send_money_action
    )

def change_pin_view(request):
    def change_pin_action(account, data):
        account.change_pin(data['old_pin'], data['new_pin'])

    return handle_form_submission(
        request,
        ChangePinForm,
        'PIN change successful!',
        'changepin.html',
        change_pin_action
    )

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
