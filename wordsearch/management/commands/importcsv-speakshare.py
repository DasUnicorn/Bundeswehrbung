from django.core.management.base import BaseCommand
from wordsearch.models import Speaker, Episode, Line
import csv
from datetime import datetime, timedelta
from pathlib import Path
from Decimal import Decimal


class Command(BaseCommand):
	help = 'Import a given csv file into wordsearch database'

	def add_arguments(self, parser):
		parser.add_argument('filenames', nargs='+', type=str)

	def handle(self, *args, **options):
		for file in options['filenames']:
			with open(file, 'r') as fp: 		#schließt Datei nach dem Block
				reader = csv.DictReader(fp)
				for row in reader:
					episode = Path('filename.csv').stem
					episode, _ = Episode.objects.get_or_create(number=row["Episode"])
					name, _ = Speaker.objects.get_or_create(name=row["Speaker"])

					# we specify the input and the format...
					time = datetime.strptime(row["Time"],"%H:%M:%S")
					percantage[:-1] = Speak_Share.Decimal(row["speak_share"])
					word_number = words(row["word_number"])

					Line.objects.create(
						episode=episode,
						speaker=speaker,
						time=time,
						speak_share=speak_share,
						word_number=word_number)