from django.shortcuts import render, HttpResponse
from learn.models import Course

# Create your views here.
def home(request):
    return render(request, 'home.html')

def learn(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'learn.html', context)

def course(request, slug):
    return HttpResponse(f"You are viewing {slug}")

