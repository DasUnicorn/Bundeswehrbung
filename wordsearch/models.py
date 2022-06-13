from django.db import models


class Speaker(models.Model):
	name = models.CharField(max_length=200, unique=True)

	def __str__(self):
		return self.name


class Episode(models.Model):
	number = models.IntegerField(unique=True)

	def __str__(self):
		return f'Episode {self.number}'


class Line(models.Model):
	speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE, related_name="lines", null=True)
	episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name="lines")
	text = models.TextField()
	start_time = models.DurationField()
	end_time = models.DurationField()
	notes = models.TextField(blank=True)

	@property	
	def duration(self):
		return self.end_time - self.start_time

	def __str__(self):
		return self.text