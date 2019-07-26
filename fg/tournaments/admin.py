from django.contrib import admin

from .models import Player, Person, Tournament, GroupAPlayer, GroupBPlayer, GroupCPlayer, GroupDPlayer, TournamentPick


admin.site.register(Person)
admin.site.register(Player)
admin.site.register(Tournament)
admin.site.register(GroupAPlayer)
admin.site.register(GroupBPlayer)
admin.site.register(GroupCPlayer)
admin.site.register(GroupDPlayer)
admin.site.register(TournamentPick)