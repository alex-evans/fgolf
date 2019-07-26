from django.core.management.base import BaseCommand, CommandError
from tournaments.models import Player, Tournament, GroupAPlayer, GroupBPlayer, GroupCPlayer, GroupDPlayer
import csv
import os

        
class Command(BaseCommand):
    help = 'Loads Tournament Groupings from {touranemnt name}_groups.csv file in fg/external_files/csvs'


    def add_arguments(self, parser):
        parser.add_argument('tournament')


    def handle(self, *args, **options):
        tournament_obj = Tournament.objects.get(name=options['tournament'])
        self.clear_groups(tournament_obj)
        self.save_groups(tournament_obj)
        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {tournament_obj.name}\'s Player Groupings'))


    def clear_groups(self, tournament_obj):
        a = GroupAPlayer.objects.filter(tournament=tournament_obj)
        b = GroupBPlayer.objects.filter(tournament=tournament_obj)
        c = GroupCPlayer.objects.filter(tournament=tournament_obj)
        d = GroupDPlayer.objects.filter(tournament=tournament_obj)
        a.delete()
        b.delete()
        c.delete()
        d.delete()


    def save_groups(self, tournament_obj):
        path = '/Users/alexevans/Desktop/Projects/fgolf/fg/external_files/csvs/'
        os.chdir(path)
        file_name = tournament_obj.file_name + "_groups.csv"
        with open(file_name, encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['A']:
                    p = self.get_player_obj(row['A'])
                    g = GroupAPlayer(tournament=tournament_obj, player=p, winnings=0)
                    g.save()
                if row['B']:
                    p = self.get_player_obj(row['B'])
                    g = GroupBPlayer(tournament=tournament_obj, player=p, winnings=0)
                    g.save()
                if row['C']:
                    p = self.get_player_obj(row['C'])
                    g = GroupCPlayer(tournament=tournament_obj, player=p, winnings=0)
                    g.save()
                if row['D']:
                    p = self.get_player_obj(row['D'])
                    g = GroupDPlayer(tournament=tournament_obj, player=p, winnings=0)
                    g.save()


    def get_player_obj(self, player_name):
        try:
            p = Player.objects.get(name=player_name)
        except Player.DoesNotExist:
            p = Player(name=player_name)
            p.save()
        return p
        

        