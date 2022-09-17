from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

from .models import Course , Info

def index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {
        'courses': courses
    })

def course(request, course_id):
    courses = Info.objects.filter(id=course_id).first()
    return render(request, 'courses/course.html', {
        'courses': courses
    })
