from django.db import models
from datetime import timedelta


class Speaker(models.Model):
	name = models.CharField(max_length=200, unique=True)
	gender = models.CharField(max_length=12, blank=True)
	age = models.PositiveSmallIntegerField(null=True, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ("name",)


class Episode(models.Model):
	number = models.IntegerField(unique=True)
	duration = models.DurationField(default=timedelta)
	spoken_time = models.DurationField(default=timedelta)
	spoken_words = models.PositiveIntegerField(default=0)
	youtube_id = models.CharField(null=True, blank=True, max_length=20)

	def __str__(self):
		return f'Episode {self.number}'

	class Meta:
		ordering = ("number",)


class Line(models.Model):
	speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE, related_name="lines", null=True)
	episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name="lines")
	text = models.TextField()
	words = models.PositiveIntegerField(default=0)
	start_time = models.DurationField()
	end_time = models.DurationField()
	notes = models.TextField(blank=True)

	@property	
	def duration(self):
		return self.end_time - self.start_time

	def youtube_link(self):
		if not self.episode.youtube_id:
			return None
		time = int(self.start_time.total_seconds())
		return f"https://www.youtube.com/watch?v={self.episode.youtube_id}&t={time}"

	def __str__(self):
		return self.text

	class Meta:
		ordering = ("episode", "start_time")

class SpeakShare(models.Model):
	episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
	time = models.DurationField()
	speak_share = models.DecimalField(max_digits=4, decimal_places=1)

	def __str__(self):
		return f'SpeakShare {self.speak_share}'

	class Meta:
		ordering = ("speak_share",)

class ShareOfSpeech(models.Model):
	speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
	episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
	duration = models.DurationField()
	words = models.PositiveIntegerField()

	def __str__(self):
		return f'TimeSpoken {self.speak_share}'

	class Meta:
		ordering = ("speaker",)


#Speaker, episode, count all durations with id speaker + id episode, count all text in episode with id speaker
