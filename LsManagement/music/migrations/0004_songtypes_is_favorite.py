# Generated by Django 2.1.1 on 2018-09-24 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_song_typeid'),
    ]

    operations = [
        migrations.AddField(
            model_name='songtypes',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
