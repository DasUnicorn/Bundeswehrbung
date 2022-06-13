# Generated by Django 4.0.5 on 2022-06-13 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordsearch', '0002_rename_episode_number_episode_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
