from django.shortcuts import redirect, render
from accounts.forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    users_list = get_user_model().objects.all()
    context = {
        'users_list':users_list,
    }
    return render(request, 'accounts/index.html', context)

def signup(request):
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('accounts:index')
    else:
        signup_form = CustomUserCreationForm()
    context = {
        'signup_form': signup_form,
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def detail(request, user_pk):
    user_detail = get_user_model().objects.get(pk=user_pk)
    context = {
        'user_detail': user_detail,
    }
    return render(request, 'accounts/detail.html', context)

def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user_login(request, login_form.get_user())
            return redirect(request.GET.get('next') or 'accounts:index')
    else:
        login_form = AuthenticationForm()
    context = {
        'login_form': login_form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    user_logout(request)
    return redirect('accounts:index')

@login_required
def update(request, user_pk):
    if request.method == 'POST':
        update_form = CustomUserChangeForm(data=request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            return redirect('accounts:index')
    else:
        update_form = CustomUserChangeForm(instance=request.user)
    context = {
        'update_form': update_form,
    }
    return render(request, 'accounts/update.html', context)

@login_required
def password(request):
    if request.method == 'POST':
        change_password_form = PasswordChangeForm(request.user, request.POST)
        if change_password_form.is_valid():
            change_password_form.save()
            return redirect('accounts:index')
    else:
        change_password_form = PasswordChangeForm(request.user)
    context = {
        'change_password_form': change_password_form,
    }
    return render(request, 'accounts/password.html', context)