from user.models import User
from classroom.models import Classroom
from student.models import Student
from subject.models import Subject
from teacher.models import Teacher
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from student.forms import StudentForm

User = get_user_model()

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

def base(request):
    show_button = request.path != '/base'
    return render(request, "base.html",{'show_button': show_button})

# for classroom view and create
def classroom_view(request):
    classrooms = Classroom.objects.all()
    context = {       
        'classrooms': classrooms,
    }
    if request.method == 'POST':
        room_number = request.POST.get('room_number')
        total_student = request.POST.get('total_student')
        new_classroom = Classroom(room_number=room_number, total_student=total_student)
        new_classroom.save()
        return redirect('/classroom/') 
    return render(request, "classroom.html",context)
# Update
def classroom_edit(request, room_number):
    classroom = get_object_or_404(Classroom, room_number=room_number)    
    if request.method == 'POST':
        room_number = request.POST.get('room_number')
        total_student = request.POST.get('total_student')
        classroom.total_student = total_student
        classroom.save()
        return redirect('/classroom/')
    context = {'classroom': classroom}
    return render(request, "classroom.html",context)
# Delete
def classroom_delete(request, room_number):
        classroom = get_object_or_404(Classroom, room_number=room_number)
        classroom.delete()
        return redirect('classroom') 

# def student_edit(request, s_id):
#     student = Student.objects.get(s_id = s_id)
#     form = StudentForm(request.POST, instance = student)  
#     if form.is_valid():  
#         form.save()  
#         return redirect("/student")  
#     return render(request, 'student.html', {'student': student})

def student_view(request):
    students = Student.objects.all()
    form = StudentForm() 
    context = {       
        'students': students,
        'form' : form
    }
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/student/')
            except Exception as e:
                print(e)
                return redirect('/student/')
        else:
            return redirect('/student/') 
    return render(request, "student.html",context)


def student_delete(request, s_id):  
    student = Student.objects.get(s_id=s_id)  
    student.delete()  
    return redirect('/student/')


    

