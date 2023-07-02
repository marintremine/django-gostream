from django.shortcuts import render

from equipe.models import Equipe, Streamer

# Create your views here.


def equipe(request):
    streamers = Streamer.objects.order_by("name")
    equipes = Equipe.objects.order_by("name")
    return render(request,'equipe/index.html', context={'streamers':streamers,'equipes':equipes})