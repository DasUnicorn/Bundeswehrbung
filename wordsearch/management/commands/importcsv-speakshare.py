from django.core.management.base import BaseCommand
from wordsearch.models import Speaker, Episode, SpeakShare
import csv
from datetime import datetime, timedelta
from pathlib import Path
from decimal import Decimal


class Command(BaseCommand):
	help = 'Import a given csv file into wordsearch database'

	def add_arguments(self, parser):
		parser.add_argument('filenames', nargs='+', type=str)

	def handle(self, *args, **options):
		for file in options['filenames']:
			with open(file, 'r') as fp: 		#schließt Datei nach dem Block
				reader = csv.DictReader(fp)
				for row in reader:
					episode_number = Path(file).stem
					episode, _ = Episode.objects.get_or_create(number=episode_number)
					speaker, _ = Speaker.objects.get_or_create(name=row["name"])

					# we specify the input and the format...
					time = datetime.strptime(row["time"],"%H:%M:%S")
					delta = timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)
					speak_share = row["percentage"][:-1]
					word_number = row["words"]


					SpeakShare.objects.create(
						episode=episode,
						speaker=speaker,
						time=delta,
						speak_share=speak_share,
						word_number=word_number)