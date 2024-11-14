# from .models import Student
# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib import messages
# from django.contrib.auth import logout

# def login_page(request):
#     if request.method == "POST":
#         try:
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user_obj = Student.objects.filter(username=username)
#             if not user_obj.exists():
#                 messages.error(request, "Username not found")
#                 return redirect('/login/')
#             user_obj = authenticate(username=username, password=password)
#             if user_obj:
#                 login(request, user_obj)
#                 return redirect('editor')
#             messages.error(request, "Wrong Password")
#             return redirect('/login/')
#         except Exception as e:
#             messages.error(request, "Something went wrong")
#             return redirect('/register/')
#     return render(request, "login.html")

# def register_page(request):
#     if request.method == "POST":
#         try:
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user_obj = Student.objects.filter(username=username)
#             if user_obj.exists():
#                 messages.error(request, "Username is taken")
#                 return redirect('/register/')
#             user_obj = Student.objects.create(username=username)
#             user_obj.set_password(password)
#             user_obj.save()
#             messages.success(request, "Account created")
#             return redirect('/login')
#         except Exception as e:
#             messages.error(request, "Something went wrong")
#             return redirect('/register')
#     return render(request, "register.html")

# def custom_logout(request):
#     logout(request)    
#     return redirect('login')


