from django.db import models


class Speaker(models.Model):
	name = models.CharField(max_length=200, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ("name",)


class Episode(models.Model):
	number = models.IntegerField(unique=True)

	def __str__(self):
		return f'Episode {self.number}'

	class Meta:
		ordering = ("number",)


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

	class Meta:
		ordering = ("episode", "start_time")

class SpeakShare(models.Model):
	episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
	speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE, null=True)
	time = models.DurationField()
	speak_share = models.DecimalField
	word_number = models.IntegerField

	def __str__(self):
		return f'SpeakShare {self.speak_share}'

	class Meta:
		ordering = ("speak_share",)