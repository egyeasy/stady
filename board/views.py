from django.shortcuts import render, redirect
from django.forms import formset_factory, modelformset_factory
from django.forms.models import BaseModelFormSet
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import SchoolRecord, Record, Test, TargetUniv, Question
from .forms import SchoolRecordForm, RecordForm, TestForm, TargetUnivForm, QuestionForm


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
    recordForm = RecordForm()
    context = {
        'recordForm': recordForm,
    }
    return render(request, 'board/fillout_record.html', context)
    
# def fillout_test(request):
#     if request.method == "POST":
#         pass
#     else:
#         testForm = TestForm()
#         context = {
#             'testForm': testForm,
#         }
#         return render(request, 'board/fillout_test.html', context)


@method_decorator(login_required, name='dispatch')
class TestFormView(View):
    Test_FormSet = modelformset_factory(Test, form=TestForm)
    
    # Overiding the get method
    def get(self, request, *args, **kwargs):
        results = Test.objects.filter(user=request.user)
        # Creating an Instance of formset and putting it in context dict
        if results:
            context = {
                'test_form': self.Test_FormSet(queryset=results)
            }
        else:
            context = {
                'test_form': self.Test_FormSet(queryset=Test.objects.none()),
            }
        return render(request, 'board/fillout_test.html', context)

    # Overiding the post method
    def post(self, request, *args, **kwargs):
        results = Test.objects.filter(user=request.user)
        if results:
            test_formset = self.Test_FormSet(request.POST, queryset=results)
        else:
            test_formset = self.Test_FormSet(request.POST)
        for test in test_formset:
            if test.is_valid():
                # Saving in the contacts models
                form = test.save(commit=False)
                form.user = request.user
                form.save()
            else:
                print("not valid, result:", results)
                if results:
                    context = {
                        'test_form': self.Test_FormSet(queryset=results),
                    }
                else:
                    context = {
                        'test_form': self.Test_FormSet(queryset=Test.objects.none()),
                    }
                return render(request, 'board/fillout_test.html', context)
        return redirect('board:fillout_target')
            

# @login_required
# def fillout_target(request):
#     if request.method == "POST":
#         pass
#     else:
#         targetUnivForm = TargetUnivForm()
#         context = {
#             'targetUnivForm': targetUnivForm,
#         }
#         return render(request, 'board/fillout_target.html', context)


@method_decorator(login_required, name='dispatch')
class TargetUnivFormView(View):
    # We are creating a formset out of the TestForm
    Target_FormSet = formset_factory(TargetUnivForm)

    # Overiding the get method
    def get(self, request, *args, **kwargs):
        # Creating an Instance of formset and putting it in context dict
        context = {
                'target_form': self.Target_FormSet(),
                }
        return render(request, 'board/fillout_target.html', context)

    # Overiding the post method
    def post(self, request, *args, **kwargs):
        print(self.request.POST)
        target_formset = self.Target_FormSet(self.request.POST)
        print(target_formset)
        for target in target_formset:
            if target.is_valid():
                # Saving in the contacts models
                form = target.save(commit=False)
                form.user = request.user
                form.save()
            else:
                context = {
                        'target_form': self.Target_FormSet(),
                    }
                return render(request, 'board/fillout_target.html', context)
        return redirect('board:fillout_question')

    
@login_required
def fillout_question(request):
    if request.method == "POST":
        questionForm = QuestionForm(request.POST)
        if questionForm.is_valid():
            form = questionForm.save(commit=False)
            form.user = request.user
            form.save()
        return redirect('board:overview')
    else:
        questionForm = QuestionForm()
        context = {
            'questionForm': questionForm,
        }
        return render(request, 'board/fillout_question.html', context)


@login_required
def overview(request):
    schoolRecord = SchoolRecord.objects.get(user=request.user)
    record = Record.objects.get(user=request.user)
    recordForm = RecordForm(instance=record)
    tests = Test.objects.filter(user=request.user)
    targetUnivs = TargetUniv.objects.filter(user=request.user).order_by('order')
    question = Question.objects.get(user=request.user)
    context = {
        'schoolRecord': schoolRecord,
        'recordForm': recordForm,
        'tests': tests,
        'targetUnivs': targetUnivs,
        'question': question,
    }
    return render(request, 'board/overview.html', context)
