from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from board.models import SchoolRecord, Record, Test, TargetUniv, Question
from board.forms import RecordForm, FeedbackForm

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
    schoolRecords = SchoolRecord.objects.filter(user=user)
    records = Record.objects.filter(user=user)
    if records:
        recordForm = RecordForm(instance=records[0])
    else:
        recordForm = None
    tests = Test.objects.filter(user=user)
    targetUnivs = TargetUniv.objects.filter(user=user).order_by('order')
    questions = Question.objects.filter(user=user)
    context = {
        'student': user,
        'schoolRecord': schoolRecords,
        'recordForm': recordForm,
        'tests': tests,
        'targetUnivs': targetUnivs,
        'questions': questions,
    }
    return render(request, 'manage/overview.html', context)


def feedback(request, student_email):
    user = get_user_model().objects.get(email=student_email)
    if request.method == 'POST':
        feedbackForm = FeedbackForm(request.POST)
        if feedbackForm.is_valid():
            form = feedbackForm.save(commit=False)
            form.user = user
            form.is_staff = True
            form.save()
            return redirect('manage:feedback', student_email=student_email)
    else:
        questions = Question.objects.filter(user=user).order_by('created_at')
        feedbackForm = FeedbackForm()
        context = {
            'student': user,
            'questions': questions,
            'feedbackForm': feedbackForm,
        }
        return render(request, 'manage/feedback.html', context)
        
        
        