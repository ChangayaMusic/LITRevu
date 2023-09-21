from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from login.models import CustomUser
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django import forms
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView

def home(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():

            login(request, form.get_user())

            return redirect('confirmation')
    else:
        form = AuthenticationForm(request)

    return render(request, 'home.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = CustomUser.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')  #
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class CustomLoginView(LoginView):
    template_name = 'home.html'

class MyLogoutView(LogoutView):
    template_name = 'login/templates/home.html'

