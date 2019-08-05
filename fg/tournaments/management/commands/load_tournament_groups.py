from django.core.management.base import BaseCommand, CommandError
from tournaments.models import Player, Tournament, TournamentPlayer
import csv
import os

        
class Command(BaseCommand):
    help = 'Loads Tournament Groupings from {touranemnt name}_groups.csv file in fg/external_files/csvs'


    def add_arguments(self, parser):
        parser.add_argument('tournament')


    def handle(self, *args, **options):
        tournament_obj = Tournament.objects.get(name=options['tournament'])
        self.save_groups(tournament_obj)
        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {tournament_obj.name}\'s Player Groupings'))


    def save_groups(self, tournament_obj):
        path = '/Users/alexevans/Desktop/Projects/fgolf/fg/external_files/csvs/'
        os.chdir(path)
        file_name = tournament_obj.file_name + "_groups.csv"
        with open(file_name, encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['A']:
                    p = self.get_player_obj(row['A'])
                    self.set_tournament_player_group(tournament_obj, p, 'A')
                if row['B']:
                    p = self.get_player_obj(row['B'])
                    self.set_tournament_player_group(tournament_obj, p, 'B')
                if row['C']:
                    p = self.get_player_obj(row['C'])
                    self.set_tournament_player_group(tournament_obj, p, 'C')
                if row['D']:
                    p = self.get_player_obj(row['D'])
                    self.set_tournament_player_group(tournament_obj, p, 'D')


    def get_player_obj(self, player_name):
        try:
            return Player.objects.get(name=player_name)
        except Player.DoesNotExist:
            print(f"ERROR: Player does not exist: {player_name}")        
        

    def set_tournament_player_group(self, tournament, player, group):
        if not player:
            return
        try:
            tp = TournamentPlayer.objects.get(tournament=tournament, player=player)
            tp.group = group
            tp.save()
        except TournamentPlayer.DoesNotExist:
            print(f"ERROR: Tournament Player does not exist: {tournament} - {player} - {group}")