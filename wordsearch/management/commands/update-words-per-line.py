import os
from django.core.management.base import BaseCommand
from wordsearch.models import Line

class Command(BaseCommand):
	help = 'Updates the amount of spoken words in each line'

	def handle(self, *args, **options):
		lines = Line.objects.all()

		for line in lines:
			words = line.text.split()
			count = len(words)

			line.words = count
			line.save()

		print("done :)")