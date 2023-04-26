# Calculating the spoken time in each episode and writing it into the database

import os
from django.core.management.base import BaseCommand
from wordsearch.models import Line, Episode
import datetime

class Command(BaseCommand):
	help = 'Import the spoken time got a number of episodes'

	def add_arguments(self, parser):
		parser.add_argument("ep", type=int)

	def handle(self, *args, **options):
		ep = options['ep']

		for e in range(1,ep+1):
			time = datetime.timedelta(0)
			episode_lines = Line.objects.filter(episode = e)

			for line in episode_lines:
				spoken_time = line.end_time - line.start_time
				time = time + spoken_time

			current_episode = Episode.objects.get(number= e)
			current_episode.spoken_time = time
			current_episode.save()