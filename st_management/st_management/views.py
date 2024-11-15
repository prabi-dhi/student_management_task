from django.urls import reverse
from user.models import User
from classroom.models import Classroom
from student.models import Student
from subject.models import Subject
from teacher.models import Teacher
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

User = get_user_model()

# base page
@login_required(login_url='/login/')
def base(request):
    users = User.objects.all()
    classrooms = Classroom.objects.all()
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()
    context = {
        'users': users,
        'classrooms': classrooms,
        'students' : students,
        'subjects' :subjects,
        'teachers' :teachers
    }

    if request.method == 'POST':
        room_number = request.POST.get('room_number')
        total_student = request.POST.get('total_student')
        new_classroom = Classroom(room_number=room_number, total_student=total_student)
        new_classroom.save()
        return redirect('/base/') 


    return render(request, "base.html",context)

# registration page
def register_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            usertype = request.POST.get('usertype')
            user_obj = User.objects.filter(username=username)
            if user_obj.exists():
                messages.error(request, "Username is taken")
                return redirect('/register/')
            user_obj = User.objects.create(username=username)
            user_obj.set_password(password)
            if hasattr(user_obj, 'usertype'):
                user_obj.usertype = usertype
            user_obj.save()
            messages.success(request, "Account created")
            return redirect('/login')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register')
    return render(request, "register.html")

# Login page
def login_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            # usertype= request.POST.get('usertype')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.error(request, "Username not found")
                return redirect('/login/')
            user_obj = authenticate(username=username, password=password)
            if user_obj:
                login(request, user_obj)
                return redirect('/base')
            messages.error(request, "Wrong Password")
            return redirect('/login/')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/login/')
    return render(request, "login.html")


@login_required(login_url='/login/')
def delete_classroom(request, room_number):
    classroom = Classroom.objects.get(pk = room_number)
    classroom.delete()
 
    return redirect('/?room_number=0')


def index(request):
    return render(request,"index.html")