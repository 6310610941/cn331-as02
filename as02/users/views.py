from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from courses.models import Course, Info
from users.models import Student
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    return render(request, 'users/index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('users:index'))
        else:
            return render(request, 'users/login.html', {
                'message': 'Invalid credentials.'
            })
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {
                'message': 'You are logged out.'
            })

def regist(request):
    courses = Course.objects.all()
    return render(request,'users/regist.html', {
        'courses': courses
    })

def remove(request):
    courses = Course.objects.all()
    return render(request,'users/remove.html', {
        'courses': courses
    })

def book(request, user_id):
    status = Info.objects.filter(status = 'available').values_list('id', flat=True)
    unstatus = Info.objects.filter(status = 'unavailable').values_list('id', flat=True)
    status_list = list(status)
    unstatus_list = list(unstatus)
    if request.method == "POST":
        adds = request.POST['subject']
        if int(adds) in unstatus_list:
            return render(request, 'users/regist.html', {
                'message': 'Seats are full.'
            })
        if int(adds) in status_list:
            subjects = Student.objects.get(pk=int(user_id) - 1)
            seat = Info.objects.filter(id=int(adds)).values_list('seat', flat=True)
            seat_list = list(seat)
            s = Info.objects.filter(id=int(adds))
            seats = seat_list[0]
            seatValue = int(seats) - 1
            status = Info.objects.filter(id=int(adds)).values_list('status', flat=True)
            s.update(seat=seatValue)
            if seatValue == 0:
                status.update(status='unavailable')
            subjects.subject.add(adds)

            return HttpResponseRedirect(reverse("users:regist"),{
                'message': 'Subject registered.'
            })
        else:
            return render(request, 'users/regist.html', {
                'message': 'Wrong ID.'
            })

def delete(request, user_id):
    if request.method == "POST":
        remove = request.POST['remove']
        subjects = Student.objects.get(pk=int(user_id) - 1)
        seat = Info.objects.filter(id=int(remove)).values_list('seat', flat=True)
        seat_list = list(seat)
        s = Info.objects.filter(id=int(remove))
        seats = seat_list[0]
        seatValue = int(seats) + 1
        status = Info.objects.filter(id=int(remove)).values_list('status', flat=True)
        s.update(seat=seatValue)
        if seatValue != 0:
            status.update(status='available')
        subjects.subject.remove(remove)
        return HttpResponseRedirect(reverse('users:remove'))

def result(request, user_id):
    sublist = Student.objects.filter(id=int(user_id)-1).values_list('subject', flat=True)
    return render(request,'users/result.html', {
        'sublist':sublist
    })