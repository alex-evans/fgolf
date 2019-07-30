from django.db import models

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
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.tournament.name + " - " + self.person.name + " - " + self.pick_a.player.name + ", " + self.pick_b.player.name + ", " + self.pick_c.player.name + ", " + self.pick_d.player.name
