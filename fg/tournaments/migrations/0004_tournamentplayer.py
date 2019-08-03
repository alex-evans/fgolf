# Generated by Django 2.2.2 on 2019-08-03 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0003_tournament_leaderboard_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='TournamentPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=1)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Player')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament')),
            ],
        ),
    ]
