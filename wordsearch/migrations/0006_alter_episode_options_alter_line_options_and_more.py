# Generated by Django 4.0.5 on 2023-02-15 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wordsearch', '0005_line_notes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='episode',
            options={'ordering': ('number',)},
        ),
        migrations.AlterModelOptions(
            name='line',
            options={'ordering': ('episode', 'start_time')},
        ),
        migrations.AlterModelOptions(
            name='speaker',
            options={'ordering': ('name',)},
        ),
        migrations.CreateModel(
            name='SpeakShare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DurationField()),
                ('speak_share', models.DecimalField(decimal_places=1, max_digits=4)),
                ('word_number', models.IntegerField()),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wordsearch.episode')),
                ('speaker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wordsearch.speaker')),
            ],
            options={
                'ordering': ('speak_share',),
            },
        ),
    ]
