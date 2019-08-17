from django.shortcuts import render
from django.contrib.auth import get_user_model
from board.models import SchoolRecord, Record, Test, TargetUniv, Question
from board.forms import RecordForm

# Create your views here.
# TODO: staff athenticate
def student_list(request):
    students = get_user_model().objects.filter(is_staff=False)
    context = {
        'students': students,
    }
    return render(request, 'manage/student_list.html', context)


def overview(request, student_email):
    user = get_user_model().objects.get(email=student_email)
    schoolRecord = SchoolRecord.objects.get(user=user)
    record = Record.objects.get(user=user)
    recordForm = RecordForm(instance=record)
    tests = Test.objects.filter(user=user)
    targetUnivs = TargetUniv.objects.filter(user=user).order_by('order')
    question = Question.objects.get(user=user)
    context = {
        'student': user,
        'schoolRecord': schoolRecord,
        'recordForm': recordForm,
        'tests': tests,
        'targetUnivs': targetUnivs,
        'question': question,
    }
    return render(request, 'manage/overview.html', context)


def feedback(request, student_email):
    
    context = {
        
    }
    return render(request, 'manage/feedback.html', context)