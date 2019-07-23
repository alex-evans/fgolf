from django.contrib import admin

from .models import Person, Tournament, GroupAPlayer, GroupBPlayer, GroupCPlayer, GroupDPlayer

admin.site.register(Tournament)
admin.site.register(Person)
admin.site.register(GroupAPlayer)
admin.site.register(GroupBPlayer)
admin.site.register(GroupCPlayer)
admin.site.register(GroupDPlayer)