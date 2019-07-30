from django.core.management.base import BaseCommand, CommandError
from tournaments.models import Player
import csv
import os


class Command(BaseCommand):
    help = 'Loads Players from players.csv file in fg/external_files/csvs'

    def handle(self, *args, **options):
        self.clear_players()
        path = '/Users/alexevans/Desktop/Projects/fgolf/fg/external_files/csvs/'
        os.chdir(path)
        with open('players.csv', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p = Player(name=row['PLAYER NAME'])
                p.save()
        self.stdout.write(self.style.SUCCESS('Successfully loaded Players'))


    def clear_players(self):
        p = Player.objects.all()
        p.delete()