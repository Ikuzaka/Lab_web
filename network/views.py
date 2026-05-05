from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'network/index.html')


def about(request):
    return HttpResponse("О сайте")


def contact(request):
    return HttpResponse("Контакты")
