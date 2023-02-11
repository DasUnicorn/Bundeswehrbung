from django.http import HttpResponse
from django.shortcuts import render
from .models import Line


def index(request):
    return render(request, 'index.html', {})

def search_results(request):
    query = request.GET.get("q")
    results = Line.objects.filter(text__icontains=query)
    return render(request, 'search_results.html', {"results": results, "query": query})

def impressum(request):
    return render(request, 'impressum.html', {})

def data(request):
    return render(request, 'data.html', {})