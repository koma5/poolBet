from django.shortcuts import render
from django.http import HttpResponse
from .models import Block, Pool

def index(request):
    return render(request, 'oddsboard/index.html', { 'blocks': Block.objects.all() })
