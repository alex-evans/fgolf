from django.db import models
from bs4 import BeautifulSoup
import requests


class Player(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    total_winnings = models.IntegerField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=200)
    file_name = models.CharField(max_length=200, blank=True)
    start_date = models.DateField('start date')
    end_date = models.DateField('end date')
    leaderboard_url = models.CharField(max_length=200, blank=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class TournamentPlayer(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    group = models.CharField(max_length=1, blank=True)
    winnings = models.IntegerField(blank=True)

    class Meta:
        ordering = ['tournament','player']

    def __str__(self):
        return f'{self.tournament} - {self.player} - {self.group}'


class TournamentPick(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    pick_a = models.ForeignKey(TournamentPlayer, on_delete=models.CASCADE, related_name='pick_a')
    pick_b = models.ForeignKey(TournamentPlayer, on_delete=models.CASCADE, related_name='pick_b')
    pick_c = models.ForeignKey(TournamentPlayer, on_delete=models.CASCADE, related_name='pick_c')
    pick_d = models.ForeignKey(TournamentPlayer, on_delete=models.CASCADE, related_name='pick_d')
    total_winnings = models.IntegerField(blank=True)

    def save(self, *args, **kwargs):
        self.total_winnings = self.pick_a.winnings + self.pick_b.winnings + self.pick_c.winnings + self.pick_d.winnings
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tournament.name + " - " + self.person.name + " - " + self.pick_a.player.name + ", " + self.pick_b.player.name + ", " + self.pick_c.player.name + ", " + self.pick_d.player.name
