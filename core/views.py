from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def HomeView(request):
    return render (request, 'core/index.html')

@login_required
def DashBoard(request):
    return render (request, 'core/dashboard.html')