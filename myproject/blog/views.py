from django.http import HttpResponse
from django.shortcuts import redirect, render

from blog.models import Blog, Student
from blog.forms import StudentForm


def home(request):
    context ={
        "name": "Subash",
        "address": "Okaldunga",
        "hobbies": "reading books"
    }
    context['blog']= Blog.objects.all()
    return render(request, 'resume.html', context)

def student_list(request):
    student_list =Student.objects.all()
    return render(request, 'student_list.html', context={'student_list':student_list})


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
        return render(request, 'student_create.html', {"form":form} )

def student_update(request,id): 
    stu_obj=Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=stu_obj)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=stu_obj)
        return render(request, 'student_create.html', {"form":form} )
