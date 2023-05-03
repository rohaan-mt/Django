from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"polls/index.html")

def form1(request):
    return render(request,"polls/form1.html")

def graphs(request):
    return render(request, "polls/graphs.html")