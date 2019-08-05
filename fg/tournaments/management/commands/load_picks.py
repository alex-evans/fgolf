from django.core.management.base import BaseCommand, CommandError
from tournaments.models import Player, Person, Tournament, TournamentPlayer, TournamentPick, GroupAPlayer, GroupBPlayer, GroupCPlayer, GroupDPlayer
import csv
import os
import sys

        
class Command(BaseCommand):
    help = 'Loads Tournament Picks from {tournament name}_picks.csv file in fg/external_files/csvs'


    def add_arguments(self, parser):
        parser.add_argument('tournament')


    def handle(self, *args, **options):
        tournament_obj = Tournament.objects.get(name=options['tournament'])
        self.clear_picks(tournament_obj)
        self.save_picks(tournament_obj)
        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {tournament_obj.name}\'s Picks'))


    def clear_picks(self, tournament_obj):
        p = TournamentPick.objects.filter(tournament=tournament_obj)
        p.delete()

    
    def save_picks(self, tournament_obj):
        # group_a_obj = GroupAPlayer.objects.filter(tournament=tournament_obj)
        # group_b_obj = GroupBPlayer.objects.filter(tournament=tournament_obj)
        # group_c_obj = GroupCPlayer.objects.filter(tournament=tournament_obj)
        # group_d_obj = GroupDPlayer.objects.filter(tournament=tournament_obj)
        path = '/Users/alexevans/Desktop/Projects/fgolf/fg/external_files/csvs/'
        os.chdir(path)
        file_name = tournament_obj.file_name + "_picks.csv"
        with open(file_name, encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                person_obj = self.get_person_obj(row['PERSON'])
                t_player_a_obj = self.get_player_obj(row['A'], tournament_obj, 'A')
                t_player_b_obj = self.get_player_obj(row['B'], tournament_obj, 'B')
                t_player_c_obj = self.get_player_obj(row['C'], tournament_obj, 'C')
                t_player_d_obj = self.get_player_obj(row['D'], tournament_obj, 'D')
                picks = TournamentPick(
                    tournament = tournament_obj,
                    person = person_obj,
                    pick_a = t_player_a_obj,
                    pick_b = t_player_b_obj,
                    pick_c = t_player_c_obj,
                    pick_d = t_player_d_obj,
                    total_winnings = 0
                )
                picks.save()
                    

    def get_person_obj(self, person_name):
        try:
            if person_name[-1:] == " ":
                person_name = person_name[:-1]
            p = Person.objects.get(name=person_name)
            return p
        except Person.DoesNotExist:
            print(f"ERROR: Person not found {person_name}")
            sys.exit()

    
    def get_player_obj(self, player_name, tournament, group):
        try:
            if player_name[-1:] == " ":
                player_name = player_name[:-1]
            p = Player.objects.get(name=player_name)
            tp = TournamentPlayer.objects.get(tournament=tournament, player=p, group=group)
            return tp
        except Player.DoesNotExist:
            print(f"ERROR: Player not found {player_name}")
            sys.exit()
        except TournamentPlayer.DoesNotExist:
            print(f"ERROR: Player not found in group, {player} - {group}")
            sys.exit()