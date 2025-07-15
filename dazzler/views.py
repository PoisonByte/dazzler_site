from django.shortcuts import render

def landing(request):
    return render(request, 'landing.html')

def home(request):
    return render(request, 'home.html')

def tour(request):
    return render(request, 'tour.html')

def merch(request):
    return render(request, 'merch.html')
# Create your views here.
