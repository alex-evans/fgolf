from django.core.management.base import BaseCommand, CommandError
from tournaments.models import Tournament, Player, TournamentPlayer
from datetime import datetime
import csv
import os
from bs4 import BeautifulSoup
import requests


class Command(BaseCommand):
    help = 'Loads Tournaments from tournaments.csv file'

    def handle(self, *args, **options):
        Tournament.objects.all().delete()
        Player.objects.all().delete()
        path = '/Users/alexevans/Desktop/Projects/fgolf/fg/external_files/csvs/'
        os.chdir(path)
        with open('tournaments.csv', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                t = Tournament(
                        name=row['TOURNAMENT'],
                        file_name=row['FILE NAME'],
                        start_date=row['START DATE'],
                        end_date=row['END DATE'],
                        leaderboard_url=row['URL']
                    )
                t.save()
                self.load_tournament_players(t)
        self.stdout.write(self.style.SUCCESS('Successfully loaded Tournaments'))


    def load_tournament_players(self, tournament):
        response = requests.get(tournament.leaderboard_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        field = soup.find_all('tr',{'class':'Table2__tr Table2__even'})
        for row in field:
            name = row.findAll('td')[1].get_text()
            if ' (a)' in name:
                name = name.replace(' (a)','')
            player_obj = self.get_player_obj(name)
            t_player_obj = self.get_tournament_player_obj(tournament, player_obj)
            t_player_obj.winnings = self.format_winnings(row.findAll('td')[8].get_text())
            t_player_obj.save()


    def get_player_obj(self, name):
        try:
            return Player.objects.get(name=name)
        except Player.DoesNotExist:
            p = Player(name=name)
            p.save()
            return p


    def format_winnings(self, winnings):
        winnings = winnings.replace('$','').replace(',','')
        if winnings == "--":
            winnings = 0
        return int(winnings)


    def get_tournament_player_obj(self, tournament, player):
        try:
            return TournamentPlayer.objects.get(tournament=tournament, player=player)
        except TournamentPlayer.DoesNotExist:
            tp = TournamentPlayer(
                tournament = tournament,
                player = player,
                group = "",
                winnings = 0
            )
            tp.save()
            return tp