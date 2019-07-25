from django.shortcuts import render
from .forms import SchoolRecordForm


# Create your views here.
def index(request):
    return render(request, 'landing.html')


def fillout(request):
    schoolRecordForm = SchoolRecordForm()
    context = {
        'schoolRecordForm': schoolRecordForm
    }
    return render(request, 'board/fillout.html', context)
