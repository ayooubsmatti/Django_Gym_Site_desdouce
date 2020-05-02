from django.shortcuts import render
from .models import Entrenador,Milestone


def index(request):
    entrenador = Entrenador.objects.all()
    milestone = Milestone.objects.all()
    return render(request,'home/index.html',{'entrenadors':entrenador,'milestones':milestone})