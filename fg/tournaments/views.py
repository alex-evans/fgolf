from django.shortcuts import get_object_or_404, render
from .models import Tournament, TournamentPick, Player
from bs4 import BeautifulSoup
import requests


def index(request):
    latest_tournament_list = Tournament.objects.order_by('-start_date')[:20]
    context = {'latest_tournament_list': latest_tournament_list}
    return render(request, 'tournaments/index.html', context)


def detail(request, tournament_id):
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    update_winnings(tournament)
    picks_obj = TournamentPick.objects.filter(tournament=tournament).order_by('total_winnings')
    return render(request, 'tournaments/detail.html', {'tournament': tournament, 'picks': picks_obj})


def update_winnings(tournament):
    url = tournament.leaderboard_url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    field = soup.find_all('tr',{'class':'Table2__tr Table2__even'})
    players = []
    for row in field:
        name = row.findAll('td')[1].get_text()
        player_obj = get_player_obj(name)
        winnings = format_winnings(row.findAll('td')[8].get_text())
        players.append([player_obj,winnings])
    print(players)


def get_player_obj(name):
    try:
        return Player.objects.get(name=name)
    except Player.DoesNotExist:
        print(f"ERROR: Player not found {name}")


def format_winnings(winnings):
        winnings = winnings.replace("$","").replace(",","")
        if winnings == "--":
            winnings = 0
        return int(winnings)
        