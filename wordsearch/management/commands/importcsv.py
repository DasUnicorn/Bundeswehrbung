from django.core.management.base import BaseCommand, CommandError
from wordsearch.models import Speaker, Episode, Line
import csv
from datetime import datetime, timedelta

class Command(BaseCommand):
	help = 'Import a given csv file into wordsearch database'

	def add_arguments(self, parser):
		parser.add_argument('filenames', nargs='+', type=str)

	def handle(self, *args, **options):
		for file in options['filenames']:
			with open(file, 'r') as fp: 		#schließt Datei nach dem Block
				reader = csv.DictReader(fp)
				for row in reader:
					episode, _ = Episode.objects.get_or_create(number=row["Episode"])
					speaker, _ = Speaker.objects.get_or_create(name=row["Speaker"])

					# we specify the input and the format...
					start = datetime.strptime(row["Start Time"],"%H:%M:%S")
					end = datetime.strptime(row["End Time"],"%H:%M:%S")

					Line.objects.create(
						speaker=speaker,
						episode=episode,
						text=row["Transcript"],
						start_time=timedelta(hours=start.hour, minutes=start.minute, seconds=start.second),
						end_time=timedelta(hours=end.hour, minutes=end.minute, seconds=end.second),
						notes=row["Notes"])
					
