# Generated by Django 2.2.2 on 2019-08-05 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_auto_20190804_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupbplayer',
            name='player',
        ),
        migrations.RemoveField(
            model_name='groupbplayer',
            name='tournament',
        ),
        migrations.RemoveField(
            model_name='groupcplayer',
            name='player',
        ),
        migrations.RemoveField(
            model_name='groupcplayer',
            name='tournament',
        ),
        migrations.RemoveField(
            model_name='groupdplayer',
            name='player',
        ),
        migrations.RemoveField(
            model_name='groupdplayer',
            name='tournament',
        ),
        migrations.AlterModelOptions(
            name='tournamentplayer',
            options={'ordering': ['tournament', 'player']},
        ),
        migrations.DeleteModel(
            name='GroupAPlayer',
        ),
        migrations.DeleteModel(
            name='GroupBPlayer',
        ),
        migrations.DeleteModel(
            name='GroupCPlayer',
        ),
        migrations.DeleteModel(
            name='GroupDPlayer',
        ),
    ]