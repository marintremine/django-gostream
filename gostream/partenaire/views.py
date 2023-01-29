from django.shortcuts import render

from partenaire.models import Partenaire

# Create your views here.

def partenaire(request):
    partenaires = Partenaire.objects.all()
    return render(request,'partenaire/index.html', context={'partenaires':partenaires})