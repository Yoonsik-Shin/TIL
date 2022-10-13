from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)

def index(request):
    user_lists = get_user_model().objects.all()
    context = {
        'user_lists': user_lists
    }
    return render(request,'accounts/index.html', context)

def detail(request, user_pk):
    user_detail = get_user_model().objects.get(id=user_pk)
    context = {
        'user_detail': user_detail,
    }
    return render(request, 'accounts/detail.html', context)

def main(request):
    return render(request, 'accounts/main.html')