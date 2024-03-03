from django.shortcuts import render

from equipe.models import Equipe, Streamer, Intervenant
from django.db.models.functions import Lower
# Create your views here.


def equipe(request):
    streamers = Streamer.objects.order_by(Lower("name"))
    equipes = Equipe.objects.order_by("ordre")
    intervenants = Intervenant.objects.order_by(Lower("name"))
    return render(request,'equipe/index.html', context={'streamers':streamers,'equipes':equipes,'intervenants':intervenants})