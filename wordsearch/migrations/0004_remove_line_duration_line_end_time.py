# Generated by Django 4.0.5 on 2022-06-13 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordsearch', '0003_alter_episode_number_alter_speaker_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='line',
            name='duration',
        ),
        migrations.AddField(
            model_name='line',
            name='end_time',
            field=models.DurationField(default=datetime.timedelta(0)),
            preserve_default=False,
        ),
    ]
