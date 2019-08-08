from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Tournament, TournamentPick, Player, TournamentPlayer
from bs4 import BeautifulSoup
import requests


def index(request):
    latest_tournament_list = Tournament.objects.order_by('-start_date')[:20]
    context = {'latest_tournament_list': latest_tournament_list}
    return render(request, 'tournaments/index.html', context)


def detail(request, tournament_id):
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    picks = TournamentPick.objects.all()
    for pick in picks:
        pick.save()
    picks_obj = TournamentPick.objects.filter(tournament=tournament).order_by('-total_winnings')
    return render(request, 'tournaments/detail.html', {'tournament': tournament, 'picks': picks_obj})


def make_picks(request, tournament_id):
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    return render(request, 'tournaments/make_picks.html', {'tournament': tournament})