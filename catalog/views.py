from django.shortcuts import render

# Create your views here.

"""(1) def index(request):


  return render(request, 'catalog\index.html', )"""

def splash(request):
    return render(request, 'catalog\splash.html')
def login(request):
    return render(request, 'catalog\login.html')
def lisence2(request):
    return render(request, 'catalog\lisence2.html')
def lisence(request):
    return render(request, 'catalog\lisence.html')
def index(request):
    return render(request, 'catalog\index.html')
def id2(request):
    return render(request, 'catalog\id2.html')
def id(request):
    return render(request, 'catalog\id.html')
def Birth3(request):
    return render(request, 'catalog\Birth3.html')
def Birth2(request):
    return render(request, 'catalog\Birth2.html')
def Birth(request):
    return render(request, 'catalog\Birth.html')