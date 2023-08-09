from django.shortcuts import render

from emissions.models import Categorie,Emission
# Create your views here.

def emissions(request):

    emissions_bd = Emission.objects.all()
    categories_bd = Categorie.objects.all()
    # for categorie in categories_bd:
    #     print(categorie.name)
    #     for emission in emissions_bd:
    #         if emission.categorie == categorie:
    #             print(emission.name)

    return render(request,'emissions/index.html',context={'emissions':emissions_bd,'categories':categories_bd})