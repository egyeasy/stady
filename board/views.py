from django.shortcuts import render, redirect
from django.forms import formset_factory, modelformset_factory, inlineformset_factory
from django.forms.models import BaseModelFormSet
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import SchoolRecord, Record, Test, TargetUniv, Question
from .forms import SchoolRecordForm, RecordForm, TestForm, TargetUnivForm, QuestionForm
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'landing.html')


@login_required
def fillout_school(request):
    if request.method == "POST":
        print(request.POST)
        schoolRecordForm = SchoolRecordForm(request.POST)
        print(request.user)
        if schoolRecordForm.is_valid():
            form = schoolRecordForm.save(commit=False)
            form.user = request.user
            form.save()
        return redirect('board:fillout_record')
    else:
        # 작성한 게 있을 때 가져와서 보여주기
        results = SchoolRecord.objects.filter(user=request.user)
        if results:
            schoolRecordForm = SchoolRecordForm(instance=results[0])
        # 작성한 게 없으면
        else:
            schoolRecordForm = SchoolRecordForm()
        context = {
            'schoolRecordForm': schoolRecordForm,
            }
        return render(request, 'board/fillout_school.html', context)


@login_required
def fillout_record(request):
    if request.method == "POST":
        form = RecordForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('board:fillout_test')
    results = Record.objects.filter(user=request.user)
    if results:
        recordForm = RecordForm(instance=results[0])
    else:
        recordForm = RecordForm()
    context = {
        'recordForm': recordForm,
    }
    return render(request, 'board/fillout_record.html', context)


@method_decorator(login_required, name='dispatch')
class TestFormView(View):
    Test_FormSet = inlineformset_factory(get_user_model(), Test, form=TestForm, extra=1)
    
    # Overiding the get method
    def get(self, request, *args, **kwargs):
        results = Test.objects.filter(user=request.user)
        context = {
                'formset': self.Test_FormSet(instance=request.user),
            }
        return render(request, 'board/fillout_test.html', context)

    # Overiding the post method
    def post(self, request, *args, **kwargs):
        test_formset = self.Test_FormSet(request.POST, instance=request.user)
        print(test_formset)
        print(" ")
        print(request.POST)
        if test_formset.is_valid():
            test_formset.save()
            return redirect('board:fillout_target')
        else:
            errors = test_formset.errors
            print(errors)
            return redirect('board:fillout_test')


@method_decorator(login_required, name='dispatch')
class TargetUnivFormView(View):
    # We are creating a formset out of the TestForm
    Target_FormSet = inlineformset_factory(get_user_model(), TargetUniv, form=TargetUnivForm, min_num=3, extra=0)
    
    # Overiding the get method
    def get(self, request, *args, **kwargs):
        context = {
                'formset': self.Target_FormSet(instance=request.user),
                }
        return render(request, 'board/fillout_target.html', context)

    # Overiding the post method
    def post(self, request, *args, **kwargs):
        target_formset = self.Target_FormSet(request.POST, instance=request.user)
        
        if target_formset.is_valid():
            target_formset.save()
            return redirect('board:fillout_question')
        else:
            errors = target_formset.errors
            print(errors)
            return redirect('board:fillout_target')

    
@login_required
def fillout_question(request):
    if request.method == "POST":
        questionForm = QuestionForm(request.POST)
        if questionForm.is_valid():
            form = questionForm.save(commit=False)
            form.user = request.user
            form.save()
        return redirect('board:fillout_question')
    else:
        questions = Question.objects.filter(user=request.user)
        questionForm = QuestionForm()
        context = {
            'questions': questions,
            'questionForm': questionForm,
        }
        return render(request, 'board/fillout_question.html', context)


@login_required
def overview(request):
    schoolRecords = SchoolRecord.objects.filter(user=request.user)
    records = Record.objects.filter(user=request.user)
    if records:
        recordForm = RecordForm(instance=records[0])
    else:
        recordForm = None
    tests = Test.objects.filter(user=request.user)
    targetUnivs = TargetUniv.objects.filter(user=request.user).order_by('order')
    questions = Question.objects.filter(user=request.user)
    context = {
        'schoolRecords': schoolRecords,
        'recordForm': recordForm,
        'tests': tests,
        'targetUnivs': targetUnivs,
        'questions': questions,
    }
    return render(request, 'board/overview.html', context)


@login_required
def register(request):
    messages.success(request, '신청이 완료되었습니다. 등록하신 이메일로 안내 메일이 발송될 예정입니다.')
    context = {
        
    }
    # return render(request, 'board/register.html', context)
    return redirect('board:overview')
