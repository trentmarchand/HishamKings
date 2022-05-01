import django_filters
from .models import *
from django_filters import DateFilter, CharFilter

class BetFilter(django_filters.FilterSet):
    equal_date = DateFilter(field_name="bet_time", lookup_expr="gte")
    note_contains = CharFilter(field_name="bet_note", lookup_expr="icontains")
    #end_date = DateFilter(field_name="bet_time", lookup_expr="lte")
    class Meta:
        model = Bet
        exclude = ['userID', 'team_selection', 'bet_time', 'bet_note']
