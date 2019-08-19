from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomConsultCreationForm
from django.contrib import messages
from django.urls import reverse


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, '회원가입이 완료되었습니다.')
        else:
            errors = str(form.errors).split('</li>')[0].split('<li>')[-1]
            print(errors)
            messages.error(request, errors)
            return redirect(request.META.get('HTTP_REFERER'))
        return redirect('board:index')
    else:
        form = CustomUserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/signup.html', context)

    
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('board:index')
        else:
            errors = str(form.errors).split('</li>')[0].split('<li>')[-1]
            print(errors)
            messages.error(request, errors)
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})
    
    
def logout(request):
    auth_logout(request)
    return redirect('board:index')


def consult_signup(request):
    if request.method == "POST":
        form = CustomConsultCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            auth_login(request, user)
        return redirect('board:index')
    else:
        form = CustomConsultCreationForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/signup.html', context)
    