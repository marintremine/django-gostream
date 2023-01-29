from django.shortcuts import render

from equipe.models import Equipe, Streamer

# Create your views here.


def equipe(request):
    streamers = Streamer.objects.all()
    equipes = Equipe.objects.all()
    return render(request,'equipe/index.html', context={'streamers':streamers,'equipes':equipes})