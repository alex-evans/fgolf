from django.shortcuts import get_object_or_404, render
from .models import Tournament, TournamentPick, Player, TournamentPlayer, GroupAPlayer, GroupBPlayer, GroupCPlayer, GroupDPlayer
from bs4 import BeautifulSoup
import requests


def index(request):
    latest_tournament_list = Tournament.objects.order_by('-start_date')[:20]
    context = {'latest_tournament_list': latest_tournament_list}
    return render(request, 'tournaments/index.html', context)


def detail(request, tournament_id):
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    players_winnings_list = tournament.get_winnings()
    for player_winnings in players_winnings_list:
        player_obj = player_winnings[0]
        winnings = player_winnings[1]
        try:
            tournament_player_obj = TournamentPlayer.objects.get(tournament=tournament, player=player_obj)
            group = tournament_player_obj.group
            if 'A' == group:
                g = GroupAPlayer.objects.get(tournament=tournament, player=player_obj)
                g.winnings = winnings
                g.save()
            elif 'B' == group:
                g = GroupBPlayer.objects.get(tournament=tournament, player=player_obj)
                g.winnings = winnings
                g.save()
            elif 'C' == group:
                g = GroupCPlayer.objects.get(tournament=tournament, player=player_obj)
                g.winnings = winnings
                g.save()
            elif 'D' == group:
                g = GroupDPlayer.objects.get(tournament=tournament, player=player_obj)
                g.winnings = winnings
                g.save()
        except TournamentPlayer.DoesNotExist:
            print(f"ERROR: Player, {player_obj}, not in TournamentPlayers") 
    picks = TournamentPick.objects.all()
    for pick in picks:
        pick.save()
    picks_obj = TournamentPick.objects.filter(tournament=tournament).order_by('total_winnings')
    return render(request, 'tournaments/detail.html', {'tournament': tournament, 'picks': picks_obj})
