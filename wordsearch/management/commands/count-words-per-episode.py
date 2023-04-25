# Counting the words in each episode and writing them inti the database

import os
from django.core.management.base import BaseCommand
from wordsearch.models import Line, Episode

class Command(BaseCommand):
	help = 'Import the number of words for a number of episodes'

	def add_arguments(self, parser):
		parser.add_argument("ep", type=int)

	def handle(self, *args, **options):
		ep = options['ep']

		for e in range(1,ep):
			count = 0
			episode_lines = Line.objects.filter(episode = e)

			for line in episode_lines:
				words = line.text.split()
				count = count + len(words)

			print("Words in episode " + str(e) + ": " + str(count))
			current_episode = Episode.objects.get(number= e)
			current_episode.spoken_words = count
			current_episode.save()