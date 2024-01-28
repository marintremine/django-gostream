from django.shortcuts import render

from .models import Programme

# Create your views here.
def programmation(request):
    
    if Programme.objects.exists():
        programme = Programme.objects.first()
    else:
        programme = False
    print(programme)
    return render(request,'programmation/index.html', {'programme': programme})