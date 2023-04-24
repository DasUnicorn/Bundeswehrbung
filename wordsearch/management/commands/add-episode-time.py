import os
from django.core.management.base import BaseCommand
from wordsearch.models import Episode
import datetime
import csv

class Command(BaseCommand):
	help = 'Import the length of each episode into wordsearch database'

	def add_arguments(self, parser):
		parser.add_argument('filenames', nargs='+', type=str)

	def handle(self, *args, **options):
		for file in options['filenames']:
			with open(file, 'r') as fp: 		#schließt Datei nach dem Block
				reader = csv.DictReader(fp)
				for row in reader:
					currentepisode = Episode.objects.get(number=row["episode"])
					print(currentepisode.duration)
					minutes = int(row["min"])
					seconds = int(row["sec"])
					time = datetime.timedelta(days=0,hours=0,minutes=minutes,seconds=seconds)
					currentepisode.duration = time
					print(time)
					currentepisode.save()