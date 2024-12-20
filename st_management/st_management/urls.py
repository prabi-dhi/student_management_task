"""
URL configuration for st_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import classroom_view
urlpatterns = [

    path('', views.base, name = 'base'),

    path('admin/', admin.site.urls),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name = 'login'),
    path('custom_logout/' ,views.custom_logout, name='logout'),

    path('classroom/',classroom_view, name='classroom'),  
    path('classroom/<int:room_number>/', views.classroom_edit, name='classroom_edit'),
    path('classroom/delete/<int:room_number>/', views.classroom_delete, name='classroom_delete'),  
    
    path('student/', views.student_view, name='student_view'), 
    path('student_edit/<int:s_id>/', views.student_edit, name='student_edit'),
    path('student/delete/<int:s_id>/', views.student_delete, name='student_delete'),

    path('teacher/', views.teacher_view, name='teacher_view'),
    path('teacher_edit/<int:id>/', views.teacher_edit, name='teacher_edit'),
    path('teacher/delete/<int:id>/', views.teacher_delete, name='teacher_delete'),

    path('subject/', views.subject_view, name='subject_view'),
    path('subject/edit/<int:sub_code>/', views.subject_edit, name = 'subject_edit'),
    path('subject/delete/<int:sub_code>/', views.subject_delete, name= 'subject_delete')
]
