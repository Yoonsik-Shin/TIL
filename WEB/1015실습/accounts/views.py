from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
  user_list = get_user_model().objects.all()
  context = {
    'user_list': user_list,
  }
  return render(request, 'accounts/index.html', context)

def signup(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return(redirect('accounts:index'))
  else:
    form = CustomUserCreationForm()
  context = {
    'form' : form,
  }    
  return render(request, 'accounts/signup.html', context)

def login(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      auth_login(request, form.get_user())
      return redirect(request.GET.get('next') or 'accounts:index')
  else:
    form = AuthenticationForm()
  context = {
    'form' : form,
  }
  return render(request, 'accounts/login.html', context)

def logout(request):
  auth_logout(request)
  return redirect('accounts:index')

def detail(request, pk):
  user_list = get_user_model().objects.get(pk=pk)
  context = {
    'user_list' : user_list,
  }
  return render(request, 'accounts/detail.html', context)

def update(request, pk):
  if request.method == 'POST':
    form = CustomUserChangeForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      return redirect('accounts:index')
  else:
    form = CustomUserChangeForm(instance=request.user)
  context = {
    'form': form,
  }
  return render(request, 'accounts/update.html', context)