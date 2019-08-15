from django.shortcuts import render
from django.contrib.auth import get_user_model


# Create your views here.
# TODO: staff athenticate
def student_list(request):
    students = get_user_model().objects.filter(is_staff=False)
    context = {
        'students': students,
    }
    return render(request, 'manage/student_list.html', context)