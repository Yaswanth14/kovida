from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def hire(request):
    return render(request,'hire.html')
