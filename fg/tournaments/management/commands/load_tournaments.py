from django.core.management.base import BaseCommand, CommandError
from tournaments.models import Tournament
from datetime import datetime
import csv
import os


class Command(BaseCommand):
    help = 'Loads Tournamens from tournaments.csv file'

    def handle(self, *args, **options):
        Tournament.objects.all().delete()
        path = '/Users/alexevans/Desktop/Projects/fgolf/fg/external_files/csvs/'
        os.chdir(path)
        with open('tournaments.csv', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p = Tournament(
                        name=row['TOURNAMENT'],
                        file_name=row['FILE NAME'],
                        start_date=row['START DATE'],
                        end_date=row['END DATE']
                    )
                p.save()
        self.stdout.write(self.style.SUCCESS('Successfully loaded Tournaments'))