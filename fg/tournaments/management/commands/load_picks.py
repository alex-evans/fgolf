from django.core.management.base import BaseCommand, CommandError
from tournaments.models import Player, Person, Tournament, TournamentPick, GroupAPlayer, GroupBPlayer, GroupCPlayer, GroupDPlayer
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
        group_a_obj = GroupAPlayer.objects.filter(tournament=tournament_obj)
        group_b_obj = GroupBPlayer.objects.filter(tournament=tournament_obj)
        group_c_obj = GroupCPlayer.objects.filter(tournament=tournament_obj)
        group_d_obj = GroupDPlayer.objects.filter(tournament=tournament_obj)
        path = '/Users/alexevans/Desktop/Projects/fgolf/fg/external_files/csvs/'
        os.chdir(path)
        file_name = tournament_obj.file_name + "_picks.csv"
        with open(file_name, encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                person_obj = self.get_person_obj(row['PERSON'])
                player_a_obj = self.get_player_obj(row['A'])
                player_b_obj = self.get_player_obj(row['B'])
                player_c_obj = self.get_player_obj(row['C'])
                player_d_obj = self.get_player_obj(row['D'])
                player_group_a_obj = self.verify_player_in_group(player_a_obj, 'A', tournament_obj)
                player_group_b_obj = self.verify_player_in_group(player_b_obj, 'B', tournament_obj)
                player_group_c_obj = self.verify_player_in_group(player_c_obj, 'C', tournament_obj)
                player_group_d_obj = self.verify_player_in_group(player_d_obj, 'D', tournament_obj)
                picks = TournamentPick(
                    tournament = tournament_obj,
                    person = person_obj,
                    pick_a = player_group_a_obj,
                    pick_b = player_group_b_obj,
                    pick_c = player_group_c_obj,
                    pick_d = player_group_d_obj,
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

    
    def get_player_obj(self, player_name):
        try:
            if player_name[-1:] == " ":
                player_name = player_name[:-1]
            p = Player.objects.get(name=player_name)
            return p
        except Player.DoesNotExist:
            print(f"ERROR: Player not found {player_name}")
            sys.exit()


    def verify_player_in_group(self, player_obj, group_type, tournament_obj):
        if group_type == 'A':
            try:
                p = GroupAPlayer.objects.get(tournament=tournament_obj, player=player_obj)
                return p
            except GroupAPlayer.DoesNotExist:
                print(f"ERROR: Player, {player_obj.name}, not in Group A")
                sys.exit()

        if group_type == 'B':
            try:
                p = GroupBPlayer.objects.get(tournament=tournament_obj, player=player_obj)
                return p
            except GroupBPlayer.DoesNotExist:
                print(f"ERROR: Player, {player_obj.name}, not in Group B")
                sys.exit()

        if group_type == 'C':
            try:
                p = GroupCPlayer.objects.get(tournament=tournament_obj, player=player_obj)
                return p
            except GroupCPlayer.DoesNotExist:
                print(f"ERROR: Player, {player_obj.name}, not in Group C")
                sys.exit()

        if group_type == 'D':
            try:
                p = GroupDPlayer.objects.get(tournament=tournament_obj, player=player_obj)
                return p
            except GroupDPlayer.DoesNotExist:
                print(f"ERROR: Player, {player_obj.name}, not in Group D")
                sys.exit()