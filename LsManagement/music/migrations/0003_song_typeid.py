# Generated by Django 2.1.1 on 2018-09-22 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_songtypes'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='typeId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='music.SongTypes'),
            preserve_default=False,
        ),
    ]
