
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from login.forms import SignUpForm
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
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debug statement
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
        else:
            print(form.errors)  # Debug statement
    else:
        form = SignUpForm()

    # Render the signup page with the form, including any error messages
    return render(request, 'signup.html', {'form': form})


    # Render the signup page with the form, including any error messages
    return render(request, 'signup.html', {'form': form})
class CustomLoginView(LoginView):
    template_name = 'home.html'

class MyLogoutView(LogoutView):
    template_name = 'login/templates/home.html'

