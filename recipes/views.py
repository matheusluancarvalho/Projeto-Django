from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('Home 1')


def sobre(request):
    return HttpResponse('Sobre1')


def contato(request):
    return HttpResponse('Contato1')
