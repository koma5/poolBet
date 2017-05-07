from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("showing future blocks here and deposit addresses to start betting per pool per block")
