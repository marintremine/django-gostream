from django.shortcuts import render

# Create your views here.
def mention(request):
    return render(request,'mention/index.html')