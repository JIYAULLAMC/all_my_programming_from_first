from django.shortcuts import render
from school.models import Student, Teacher

# Create your views here.


def home(request):
    # student_data = Student.objects.all()
    # student_data = Student.objects.filter(marks=98)
    # student_data = Student.objects.exclude(marks=98)
    # student_data = Student.objects.order_by('?')

    qs1 = Student.objects.values_list("name", named=True)
    qs2 = Teacher.objects.values_list("name", named=True)
    student_data = qs2.intersection(qs1)

    print("-------------------------")
    print("queryset : ", student_data)
    print("----------------------------")
    print("query  :", student_data.query)
    print("------------------------------")

    return render(request, 'school/home.html', {"students":student_data})