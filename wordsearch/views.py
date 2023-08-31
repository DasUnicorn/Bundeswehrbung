from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.db.models import F, DurationField, Sum, ExpressionWrapper
from django.db.models import Avg, Max, Min
from django.db.models import Q
from datetime import datetime, time, timedelta
from .models import Line, Speaker, Episode

def index(request):
    return render(request, 'index.html', {})

def search_results(request):
    query = request.GET.get("q")
    results = Line.objects.filter(text__icontains=query)

    return render(request, 'search_results.html', {"results": results, "query": query})

def impressum(request):
    return render(request, 'impressum.html', {})

def data(request):
    speaker_number = Speaker.objects.count()
    episode_number = Episode.objects.count()

    # Getting total time
    sum_time = Episode.objects.aggregate(total_time=Sum('duration'))
    total_time = sum_time.get('total_time')

    # Counting individual words and the number they occur
    text_list = Line.objects.values('text')
    word_count = 0
    word_list = []
    for obj in text_list:
        text = obj.get('text')
        words = text.split()
        for word in words:
            word = word.lower()
            word =  word.translate({ ord(c): None for c in "._!,'? " })
            if word in word_list:
                index = word_list.index(word)
                word_list[index+1] += 1
            else:
                word_list.append(word)
                word_list.append(1)
    word_count = int(len(word_list)/2)

    # Getting Speaker by gender
    female_speaker = Speaker.objects.filter(gender="female").count()
    male_speaker = Speaker.objects.filter(gender="male").count()

    # Getting the spoken time in total
    duration_per_line = Line.objects.annotate(time=(F("end_time") - F("start_time")))
    spoken_time_total = duration_per_line.aggregate(time_total=Sum('time'))
    spoken_time = spoken_time_total.get('time_total')

    # Spoken time per episode
    spoken_time_per_eps = duration_per_line.values('episode').annotate(time=Sum('time')).order_by()

    #Avg Spoken time per episode
    spoken_time_avg = spoken_time_per_eps.aggregate(Avg('time'))
    spoken_time_eps_avg = spoken_time_avg.get('time__avg')
    #Max and min spoken time per episode, including episode
    spoken_time_max = spoken_time_per_eps.order_by('-time')[0]
    spoken_time_min = spoken_time_per_eps.order_by('time')[0]
    max_time_esp_name = spoken_time_max.get('episode')
    max_time_esp = spoken_time_max.get('time')
    min_time_esp_name = spoken_time_min.get('episode')
    min_time_esp = spoken_time_min.get('time')

    #Spoken time by gender
    spoken_time_female = duration_per_line.filter(speaker__gender="female").aggregate(Sum('time'))
    spoken_time_male = duration_per_line.filter(speaker__gender="male").aggregate(Sum('time'))
    spoken_time_m = spoken_time_male.get('time__sum')
    spoken_time_f = spoken_time_female.get('time__sum')

    #Spoken Time by speaker
    spoken_time_per_spk = duration_per_line.values('speaker__name').annotate(time=Sum('time')).order_by()
    max_speaker = spoken_time_per_spk.order_by('-time')[0]
    min_speaker = spoken_time_per_spk.order_by('time')[0]
    max_speaker_name = max_speaker.get('speaker__name')
    max_speaker_time = max_speaker.get('time')
    min_speaker_name = min_speaker.get('speaker__name')
    min_speaker_time = min_speaker.get('time')


    return render(request, 'data.html', {
        "speaker_number": speaker_number, 
        "episode_number": episode_number, 
        "total_time": total_time, 
        "word_list": word_list, 
        "word_count": word_count,
        "female_speaker": female_speaker,
        "male_speaker": male_speaker,
        "spoken_time": spoken_time,
        "spoken_time_female": spoken_time_f,
        "spoken_time_male": spoken_time_m,
        "max_speaker_name": max_speaker_name,
        "max_speaker_time": max_speaker_time,
        "min_speaker_name": min_speaker_name,
        "min_speaker_time": min_speaker_time,
        "max_spoken_time_eps": max_time_esp_name,
        "max_spoken_time_eps_time": max_time_esp,
        "min_spoken_time_eps": min_time_esp_name,
        "min_spoken_time_eps_time": min_time_esp,
        "spoken_time_eps_avg": spoken_time_eps_avg })