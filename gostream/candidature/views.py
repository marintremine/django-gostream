
from django.shortcuts import render

# Create your views here.
def candidature(request):
    return render(request,'candidature/index.html')