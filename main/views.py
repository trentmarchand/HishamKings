from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bet, Game
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import BetForm, AccountForm


# Create your views here.

def homepage(request):
    return render(request= request,
                  template_name= "main/home.html",
                  context= {"bets": Bet.objects.all})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account Created Successfully: {username}")
            login(request, user)
            messages.info(request, f"{username} is now logged in")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")


    form = UserCreationForm
    return render(request,
                  "main/register.html",
                  context= {"form": form})

def sportsbookpage(request):
    if request.method == "POST":
        form = BetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:homepage")


    form = BetForm()
    return render(request= request,
                  template_name= "main/sportsbook.html",
                  context= {"form": form})

def accountpage(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:homepage")


    form = AccountForm()
    return render(request= request,
                  template_name= "main/account.html",
                  context= {"form": form})

def logout_request(request):
    logout(request)
    messages.info(request, f"Logged out successfully.")
    return redirect("main:login")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"{username} is now logged in")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password")

        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request,
                  "main/login.html",
                  {"form":form})