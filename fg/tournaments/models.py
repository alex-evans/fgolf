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
    
    def get_winnings(self):
        response = requests.get(self.leaderboard_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        field = soup.find_all('tr',{'class':'Table2__tr Table2__even'})
        players_winnings_list = []
        for row in field:
            name = row.findAll('td')[1].get_text()
            player_obj = self.get_player_obj(name)
            winnings = self.format_winnings(row.findAll('td')[8].get_text())
            players_winnings_list.append([player_obj,winnings])
        return players_winnings_list

    def get_player_obj(self, name):
        try:
            return Player.objects.get(name=name)
        except Player.DoesNotExist:
            print(f"ERROR: Player not found {name}")
    
    def format_winnings(self, winnings):
        winnings = winnings.replace('$','').replace(',','')
        if winnings == "--":
            winnings = 0
        return int(winnings)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class TournamentPlayer(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    group = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.tournament} - {self.player} - {self.group}'


class GroupAPlayer(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    winnings = models.IntegerField(blank=True)

    class Meta:
        ordering = ['tournament','player']

    def __str__(self):
        return self.tournament.name + " - " + self.player.name


class GroupBPlayer(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    winnings = models.IntegerField(blank=True)

    class Meta:
        ordering = ['tournament','player']

    def __str__(self):
        return self.tournament.name + " - " + self.player.name


class GroupCPlayer(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    winnings = models.IntegerField(blank=True)

    class Meta:
        ordering = ['tournament','player']

    def __str__(self):
        return self.tournament.name + " - " + self.player.name


class GroupDPlayer(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    winnings = models.IntegerField(blank=True)

    class Meta:
        ordering = ['tournament','player']

    def __str__(self):
        return self.tournament.name + " - " + self.player.name


class TournamentPick(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    pick_a = models.ForeignKey(GroupAPlayer, on_delete=models.CASCADE)
    pick_b = models.ForeignKey(GroupBPlayer, on_delete=models.CASCADE)
    pick_c = models.ForeignKey(GroupCPlayer, on_delete=models.CASCADE)
    pick_d = models.ForeignKey(GroupDPlayer, on_delete=models.CASCADE)
    total_winnings = models.IntegerField(blank=True)

    def save(self, *args, **kwargs):
        self.total_winnings = self.pick_a.winnings + self.pick_b.winnings + self.pick_c.winnings + self.pick_d.winnings
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tournament.name + " - " + self.person.name + " - " + self.pick_a.player.name + ", " + self.pick_b.player.name + ", " + self.pick_c.player.name + ", " + self.pick_d.player.name
