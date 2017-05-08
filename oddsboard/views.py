from django.shortcuts import render
from django.http import HttpResponse
from .models import Block, Pool

def index(request):
    return render(request, 'oddsboard/index.html', { 'blocks': Block.objects.all() })

def detail(request, blockHeight):
    block = Block.objects.filter(height=blockHeight)[0]
    return render(request, 'oddsboard/detail.html', { 'block': block })
