# Generated by Django 4.0.5 on 2023-03-08 21:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wordsearch', '0012_alter_speaker_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='duration',
            field=models.DurationField(default=datetime.timedelta),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episode',
            name='spoken_time',
            field=models.DurationField(default=datetime.timedelta),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='episode',
            name='spoken_words',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='speaker',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='gender',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.CreateModel(
            name='ShareOfSpeech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.DurationField()),
                ('words', models.PositiveIntegerField()),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wordsearch.episode')),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wordsearch.speaker')),
            ],
            options={
                'ordering': ('speaker',),
            },
        ),
    ]