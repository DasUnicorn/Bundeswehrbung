# Generated by Django 4.0.5 on 2022-06-13 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordsearch', '0004_remove_line_duration_line_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
