# Generated by Django 2.2.2 on 2019-08-02 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_tournamentpick_total_winnings'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='leaderboard_url',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
