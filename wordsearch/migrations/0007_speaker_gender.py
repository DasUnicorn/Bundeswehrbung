# Generated by Django 4.0.5 on 2023-02-15 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordsearch', '0006_alter_episode_options_alter_line_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='gender',
            field=models.TextField(blank=True),
        ),
    ]