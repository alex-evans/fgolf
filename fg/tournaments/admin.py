from django.contrib import admin

from .models import Player, Person, Tournament, TournamentPlayer, TournamentPick


admin.site.register(Person)
admin.site.register(Player)
admin.site.register(Tournament)
admin.site.register(TournamentPlayer)
admin.site.register(TournamentPick)