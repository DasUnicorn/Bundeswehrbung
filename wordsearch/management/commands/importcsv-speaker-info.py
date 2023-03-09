import os
from django.core.management.base import BaseCommand
from wordsearch.models import Speaker
import csv

class Command(BaseCommand):
	help = 'Import a given csv file with speaker information into wordsearch database'

	def add_arguments(self, parser):
		parser.add_argument('filenames', nargs='+', type=str)

	def handle(self, *args, **options):
		for file in options['filenames']:
			with open(file, 'r') as fp: 		#schließt Datei nach dem Block
				reader = csv.DictReader(fp)
				for row in reader:
					currentspeaker = Speaker.objects.get(name=row["name"])
					print(currentspeaker.gender)
					currentspeaker.gender = row["gender"]
					print(row["gender"])
					currentspeaker.age = row["age"]
					currentspeaker.save()