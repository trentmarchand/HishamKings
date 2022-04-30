from django.contrib import admin
from .models import Bet, Game, PaymentMethod

# Register your models here.

class BetAdmin(admin.ModelAdmin):
    # fields = ["team_selection",
    #           "bet_amount",
    #           "bet_note",
    #           "bet_time"]

    fieldsets = [("Bet Selections", {"fields": ["team_selection", "bet_amount"]}),
                 ("Game", {"fields": ["gameID"]}),
                 ("Bet Info", {"fields": ["bet_time"]}),
                 ("Additional Info", {"fields": ["bet_note"]})
    ]


admin.site.register(PaymentMethod)

admin.site.register(Game)

admin.site.register(Bet, BetAdmin)