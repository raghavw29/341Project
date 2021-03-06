# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('charID', models.IntegerField(default=121, primary_key=True, serialize=False)),
                ('charName', models.CharField(max_length=40, unique=True, verbose_name='Character Name')),
                ('charClass', models.CharField(default='Warrior', max_length=20, verbose_name='Class')),
                ('attributes', models.IntegerField(default=5)),
                ('location', models.CharField(default='No location', max_length=20)),
                ('alliance', models.CharField(choices=[('G', 'GOOD'), ('E', 'EVIL')], default='G', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemID', models.AutoField(primary_key=True, serialize=False)),
                ('itemName', models.CharField(max_length=20, verbose_name='Item Name')),
                ('desc', models.CharField(default='No description', max_length=100, verbose_name='Description')),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uName', models.CharField(max_length=40, verbose_name='Username')),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
