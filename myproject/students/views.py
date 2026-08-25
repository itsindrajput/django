from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        'title': 'Contact',
    }
    return render(request, 'contact.html', context)

def student_list(request):
    student =  Student.objects.all()
    return render(request, 'displayData.html', {'student':student})

