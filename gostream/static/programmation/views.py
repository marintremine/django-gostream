from django.shortcuts import render

from programmation.models import Programme

# Create your views here.
def programmation(request):
    programmes = Programme.objects.all()
    return render(request,'programmation/index.html',context={'programmes':programmes})