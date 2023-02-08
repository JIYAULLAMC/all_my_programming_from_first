from django.shortcuts import render
from stuapp.models import Student
from stuapp.form import StudentForm
from django.http import HttpResponse

# Create your views here.

def sboot(request):
    return render(request, 'boot.html')

def shome(request):
    return render(request, 'home.html')

def slist(request):
    students = Student.objects.all()
    return render(request, 'home.html',{"students": students})

def studata(request,pk):
    studata = Student.objects.get(id=pk)
    return render(request,'home.html',{'studata' : studata})
    

def screate(request):
    stu_form = StudentForm()
    if request.method == 'POST':       
        stu_form_data = StudentForm(request.POST)
        if stu_form_data.is_valid():
            stu_form_data.save()
            return HttpResponse("the data is saved ")
        else:
            return HttpResponse("create proper data")
    return render(request,'screate.html',{'stu_form':stu_form})

def supdate(request,pk):
    student = Student.objects.get(id=pk)
    stu_update_form = StudentForm(instance=student)
    if request.method == 'POST':
        student_form_data = StudentForm(request.POST, instance=student)
        if student_form_data.is_valid():
            student_form_data.save()
            return HttpResponse("the data is successfully updated")
        else :
            return HttpResponse("invalid input ")
    return render(request, 'screate.html',{"stu_update_form":stu_update_form})
    
