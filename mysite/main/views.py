from django.shortcuts import render

from main.models import Cafe

def index(request):
    return render(request, 'main/index.html')

def cafelist(request):
    cafes = Cafe.objects.all()
    context = {
        'cafes': cafes
    }
    return render(request, 'main/cafelist.html', context)

def cafedetails(request,pk):
    cafe = Cafe.objects.get(pk=pk)
    context = {
        'cafe' : cafe
    }
    return render(request, 'main/cafedetails.html', context)