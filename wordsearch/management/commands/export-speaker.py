import os
from django.core.management.base import BaseCommand
from wordsearch.models import Speaker, Episode, SpeakShare
import csv

speaker_list = Speaker.objects.all()

with open('speaker.txt', 'w') as f:
	for speaker in speaker_list:
		print(speaker.name, file=f)