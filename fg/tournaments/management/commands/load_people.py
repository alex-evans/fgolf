from django.core.management.base import BaseCommand, CommandError
from tournaments.models import Person
import csv
import os


class Command(BaseCommand):
    help = 'Loads People from person.csv file in fg/external_files/csvs'

    def handle(self, *args, **options):
        path = '/Users/alexevans/Desktop/Projects/fgolf/fg/external_files/csvs/'
        os.chdir(path)
        with open('people.csv', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p = Person(
                        name=row['NAME'],
                        email=row['EMAIL'],
                        total_winnings=0
                    )
                p.save()
        self.stdout.write(self.style.SUCCESS('Successfully loaded People'))
