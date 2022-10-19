from django.shortcuts import render, redirect
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        user_create_form = CustomUserCreationForm(request.POST)
        if user_create_form.is_valid():
            user_create_form.save()
            return redirect('accounts:signup')
    user_create_form = CustomUserCreationForm()
    context = {
        'user_create_form': user_create_form,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        user_login_form = AuthenticationForm(request, data=request.POST)
        if user_login_form.is_valid():
            auth_login(request, user_login_form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    user_login_form = AuthenticationForm()
    context = {
        'user_login_form': user_login_form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    messages.warning(request, '로그아웃 하였습니다.')
    return redirect('articles:index')

def account_update(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('accounts:account_detail', request.user.pk)
    user_change_form = CustomUserChangeForm(instance=request.user)
    context = {
        'user_change_form': user_change_form,
    }
    return render(request, 'accounts/update.html', context)

def account_detail(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    context = {
        'user': user,
    }
    return render(request, 'accounts/detail.html', context)