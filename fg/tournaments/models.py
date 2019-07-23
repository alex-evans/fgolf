from django.db import models


class Tournament(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    
    def __str__(self):
        return self.name


class GroupAPlayer(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    winnings = models.IntegerField()

    def __str__(self):
        return self.name


class GroupBPlayer(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    winnings = models.IntegerField()

    def __str__(self):
        return self.name


class GroupCPlayer(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    winnings = models.IntegerField()

    def __str__(self):
        return self.name


class GroupDPlayer(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    winnings = models.IntegerField()

    def __str__(self):
        return self.name


class Person(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    pick_a = models.ForeignKey(GroupAPlayer, on_delete=models.CASCADE)
    pick_b = models.ForeignKey(GroupBPlayer, on_delete=models.CASCADE)
    pick_c = models.ForeignKey(GroupCPlayer, on_delete=models.CASCADE)
    pick_d = models.ForeignKey(GroupDPlayer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
