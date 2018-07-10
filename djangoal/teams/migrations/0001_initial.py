# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 00:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
                ('position', models.CharField(choices=[('GK', 'Goalkeeper'), ('CB', 'Center fullback'), ('SW', 'Sweeper'), ('LFB', 'Left fullback'), ('RFB', 'Right fullback'), ('WB', 'Wingback'), ('LM', 'Left midfield'), ('RM', 'Right midfield'), ('DM', 'Defensive midfield'), ('CM', 'Center midfield'), ('WM', 'Wide midfield'), ('CF', 'Center forward'), ('AM', 'Attacking midfield'), ('S', 'Striker'), ('SS', 'Second striker'), ('LW', 'Left winger'), ('RW', 'Right winger')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('practice_location', models.CharField(max_length=255)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='teams.Team'),
        ),
    ]
