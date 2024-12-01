from django.shortcuts import render
from .models import Course


def course_list(request):
    title = request.GET.get('title')
    igredients = request.GET.get('igredients')
    description = request.GET.get('description')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    max_students = request.GET.get('max_students')
    print(title, description, start_date, end_date, max_students)
    if title is not None and description is not None and start_date is not None and end_date is not None and max_students is not None:
        Course.objects.create(
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            max_students=max_students,
        )
    courses = Course.objects.all()
    ctx = {'courses': courses}
    return render(request, 'courses/courses_list.html', ctx)
