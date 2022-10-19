from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['username','last_name','first_name','email','password1','password2']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ['last_name','first_name','email']