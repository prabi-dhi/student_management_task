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
from student.forms import StudentForm
from teacher.forms import TeacherForm
from subject.forms import SubjectForm

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
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.error(request, "Username not found")
                return redirect('/login/')
            user_obj = authenticate(username=username, password=password)
            if user_obj:
                login(request, user_obj)
                return redirect('/')
            messages.error(request, "Wrong Password")
            return redirect('/login/')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/login/')
    return render(request, "login.html")

@login_required(login_url='/login/')
def base(request):
    show_button = request.path != '/base'
    context = {'show_button': show_button}
    return render(request, "base.html",context)

# for classroom
@login_required(login_url='/login/')
def classroom_view(request):   #add
    classrooms = Classroom.objects.filter(is_deleted = False)
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
#update
@login_required(login_url='/login/')

def classroom_edit(request, room_number):
    classroom = Classroom.objects.get(room_number= room_number, is_deleted = False)
    if request.method == 'POST':
        total_student = request.POST.get('total_student')
        classroom.total_student = total_student
        classroom.save()
        return redirect('/classroom/')
    context = {'classroom': classroom}
    return render(request, "classroom.html",context)
# Delete
@login_required(login_url='/login/')

def classroom_delete(request, room_number):
        classroom = Classroom.objects.get( room_number=room_number)
        classroom.is_deleted= True
        classroom.save()
        return redirect('classroom') 

# For student
@login_required(login_url='/login/')
def student_view(request):
    students = Student.objects.filter(is_deleted = False)
    form = StudentForm() 
    context = {       
        'students': students,
        'form' : form
    }
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/student/')
    return render(request, "student.html",context)
@login_required(login_url='/login/')
def student_delete(request, s_id):  
    student = Student.objects.get(s_id=s_id, is_deleted = False)  
    student.is_deleted = True
    student.save()
    return redirect('/student/')
@login_required(login_url='/login/')
def student_edit(request, s_id):
    instance = Student.objects.get(s_id = s_id, is_deleted=False)
    edit_form = StudentForm(request.POST or None, instance=instance)
    if edit_form.is_valid():
        edit_form.save()
        return redirect('/student/')  
    add_form = StudentForm()

    context = {
               'edit_form': edit_form,
               'form':add_form,
               'edit_instance':instance}
    return render(request, 'student.html',context)

# For teacher
@login_required(login_url='/login/')
def teacher_view(request):
    teachers = Teacher.objects.filter(is_deleted=False)
    form = TeacherForm() 
    context = {       
        'teachers': teachers,
        'form' : form
    }
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/teacher/') 
    return render(request,'teacher.html',context)
@login_required(login_url='/login/')
def teacher_edit(request, id):
    instance = Teacher.objects.get(id=id, is_deleted=False)
    edit_form = TeacherForm(request.POST or None, instance=instance)

    if edit_form.is_valid():
        edit_form.save()
        return redirect('/teacher/')

    add_form = TeacherForm()
    context = {
        'form': add_form, 
        'edit_form': edit_form, 
        'edit_instance': instance,  
    }
    return render(request, 'teacher.html', context)
@login_required(login_url='/login/')
def teacher_delete(request,id):  
    teacher = Teacher.objects.get(id=id)  
    teacher.is_deleted = True
    teacher.save() 
    return redirect('/teacher/')

# For subject  
@login_required(login_url='/login/')  
def subject_view(request):
    subjects = Subject.objects.filter(is_deleted=False)
    form = SubjectForm() 
    context = {       
        'subjects': subjects,
        'form' : form
    }
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/subject/') 
    return render(request,'subject.html',context)
@login_required(login_url='/login/')
def subject_edit(request, sub_code):
    instance= Subject.objects.get(sub_code=sub_code,is_deleted=False)
    edit_form = SubjectForm(request.POST or None, instance=instance)
    if edit_form.is_valid():
        edit_form.save()
        return redirect('/subject/')
    add_form = SubjectForm()
    context = {
        'form': add_form,
        'edit_form': edit_form,
        'edit_instance': instance,         
    }
    return render(request, 'subject.html', context)

@login_required(login_url='/login/')
def subject_delete(request, sub_code):
    subject = Subject.objects.get(sub_code=sub_code)
    subject.is_deleted = True
    subject.save()
    return redirect('/subject/')

def custom_logout(request):
    logout(request)    
    return redirect('login')

