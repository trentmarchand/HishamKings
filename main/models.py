from django.db import models
from django.conf import settings
import uuid
import datetime

home = 'Home'
away = 'Away'
team_selection_choices =  (
    (home, 'Home team'),
    (away, 'Away team'),
)


class Game(models.Model):
    abbreviation = models.CharField(max_length=30, default=1)
    team1 = models.CharField(max_length=30)
    team2 = models.CharField(max_length=30)
    spread = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return self.abbreviation

# Create your models here.
class Bet(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    team_selection = models.CharField(
        max_length=30,
        choices=team_selection_choices,
        default=home
    )
    bet_amount = models.IntegerField()
    bet_time = models.DateTimeField(default= datetime.datetime.now())
    bet_note = models.CharField(max_length=200)
    gameID = models.ForeignKey(Game, blank=True, on_delete=models.CASCADE)
    userID = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )

    #def __str__(self):
    #    return self.bet_note

TITLE_CHOICES = [
    ('Visa', 'Visa'),
    ('Mastercard', 'Mastercard'),
    ('American Express', 'American Express'),
]

class Account(models.Model):
    balance = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
    userID = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )
    # def __str__(self):
    #     return self.userID

class PaymentMethod(models.Model):
    amount = models.IntegerField(default=0.00)
    ccn = models.CharField(max_length=100)
    card_type = models.CharField(max_length=30, choices=TITLE_CHOICES)
    exp_date = models.DateField(default= datetime.date.today())
    cvv = models.IntegerField()
    userID = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return self.ccn
