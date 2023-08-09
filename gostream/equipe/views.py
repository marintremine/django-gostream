from django.shortcuts import render

from equipe.models import Equipe, Streamer
from django.db.models.functions import Lower
# Create your views here.


def equipe(request):
    streamers = Streamer.objects.order_by(Lower("name"))
    equipes = Equipe.objects.order_by("ordre")
    return render(request,'equipe/index.html', context={'streamers':streamers,'equipes':equipes})