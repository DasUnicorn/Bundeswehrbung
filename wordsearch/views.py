from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.db.models import F, DurationField, Sum, ExpressionWrapper
from datetime import datetime, time, timedelta
from .models import Line, Speaker, Episode

def index(request):
    return render(request, 'index.html', {})

def search_results(request):
    query = request.GET.get("q")
    results = Line.objects.filter(text__icontains=query)
    return render(request, 'search_results.html', {"results": results, "query": query})

def impressum(request):
    return render(request, 'impressum.html', {""})

def data(request):
    speaker_number = Speaker.objects.count()
    episode_number = Episode.objects.count()

    # Getting total time
    duration_list = Episode.objects.all()
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
    female_speaker = len(Speaker.objects.filter(gender="female"))
    male_speaker = len(Speaker.objects.filter(gender="male"))

    return render(request, 'data.html', {
        "speaker_number": speaker_number, 
        "episode_number": episode_number, 
        "total_time": total_time, 
        "word_list": word_list, 
        "word_count": word_count,
        "female_speaker": female_speaker,
        "male_speaker": male_speaker})