from django.contrib import admin

from .models import Speaker, Episode, Line, SpeakShare


@admin.register(Line)
class LineAdmin(admin.ModelAdmin):
    list_display = ["episode", "speaker", "start_time", "end_time"]

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    pass

@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    pass


@admin.register(SpeakShare)
class SpeakShareAdmin(admin.ModelAdmin):
    pass


