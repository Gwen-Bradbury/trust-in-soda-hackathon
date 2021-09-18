from django.shortcuts import render

# Create your views here.

def index(request):
    """ Returns index.html """
    return render(request, 'home/index.html')
    