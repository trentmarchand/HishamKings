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
        fields = '__all__'