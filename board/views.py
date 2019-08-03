from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.views import View
from django.contrib.auth.decorators import login_required
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
        # 작성한 게 없으면
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


class TestFormView(View):
    # We are creating a formset out of the TestForm
    Test_FormSet = formset_factory(TestForm)

    # Overiding the get method
    def get(self, request, *args, **kwargs):
        # Creating an Instance of formset and putting it in context dict
        context = {
                'test_form': self.Test_FormSet(),
                }
        return render(request, 'board/fillout_test.html', context)

    # Overiding the post method
    def post(self, request, *args, **kwargs):
        test_formset = self.Test_FormSet(self.request.POST)
        for test in test_formset:
            if test.is_valid():
                # Saving in the contacts models
                form = test.save(commit=False)
                form.user = request.user
                form.save()
            else:
                context = {
                        'test_form': self.Test_FormSet(),
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
        target_formset = self.Target_FormSet(self.request.POST)
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
    
    context = {
        
    }
    return render(request, 'board/fillout_overview.html', context)
