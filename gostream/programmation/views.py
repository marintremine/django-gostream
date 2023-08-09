from django.shortcuts import render

# Create your views here.
def programmation(request):
    return render(request,'programmation/index.html')