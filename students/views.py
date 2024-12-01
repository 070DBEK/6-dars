from django.shortcuts import render
from .models import Student


def students_list(request):
    first_name  = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    email = request.GET.get('email')
    date_of_birth  = request.GET.get('date_of_birth')
    gender = request.GET.get('gender')
    address = request.GET.get('address')
    if first_name is not None and last_name is not None and date_of_birth is not None and gender is not None and email is not None and address is not None:
        Student.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            date_of_birth = date_of_birth,
            gender = gender,
            address = address,
        )
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students/students_list.html', ctx)