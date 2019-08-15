from django.shortcuts import render


# Create your views here.
def student_list(request):
    
    context = {
        
    }
    return render(request, 'manage/student_list.html', context)