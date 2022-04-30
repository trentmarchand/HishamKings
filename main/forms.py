from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Bet, Game, PaymentMethod
#from .models import team_selection_choices

class BetForm(ModelForm):
    #team_selection = forms.ChoiceField(choices=team_selection_choices)
    class Meta:
        model = Bet
        exclude = ['userID']

class PaymentForm(ModelForm):
    class Meta:
        model = PaymentMethod
        exclude = ['userID']


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')