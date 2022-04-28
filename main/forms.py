from django.forms import ModelForm
from .models import Bet, Game, Account
#from .models import team_selection_choices

class BetForm(ModelForm):
    #team_selection = forms.ChoiceField(choices=team_selection_choices)
    class Meta:
        model = Bet
        fields = '__all__'

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'