from django.shortcuts import render
from django.http import HttpResponse

def HomeView(request):
    return render (request, 'core/index.html')

def DashBoard(request):
    return render (request, 'core/dashboard.html')