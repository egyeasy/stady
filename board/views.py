from django.shortcuts import render, redirect
from .forms import SchoolRecordForm, TargetUnivForm


# Create your views here.
def index(request):
    return render(request, 'landing.html')


def fillout_school(request):
    
    if request.method == "POST":
        print(request.POST)
        schoolRecordForm = SchoolRecordForm(request.POST)
        if schoolRecordForm.is_valid():
            form = schoolRecordForm.save(commit=False)
            form.user = request.user
            form.save()
        return redirect('board:fillout_test')
    else:
        # 작성한 게 있을 때 가져와서 보여주기
        # 작성한 게 없으면
        schoolRecordForm = SchoolRecordForm()
        context = {
            'schoolRecordForm': schoolRecordForm,
            }
        return render(request, 'board/fillout_school.html', context)


def fillout_test(request):
    if request.method == "POST":
        pass
    else:
        context = {
            
        }
        return render(request, 'board/fillout_test.html', context)


def fillout_target(request):
    if request.method == "POST":
        pass
    else:
        targetUnivForm = TargetUnivForm()
        context = {
            'targetUnivForm': targetUnivForm,
        }
        return render(request, 'board/fillout_target.html', context)



def fillout_question(request):
    if request.method == "POST":
        pass
    else:
        
        context = {
        }
        return render(request, 'board/fillout_question.html', context)

