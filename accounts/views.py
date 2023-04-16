from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from .forms import SignUpForm, UserLoginForm, PatientRegistrationForm, DoctorRegistrationForm
from django.contrib.auth.decorators import login_required

User = get_user_model()

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = SignUpForm()
    return render (request=request, template_name="main/signup.html", context={"register_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You've successfully logged out")
    return redirect("home")

def login_request(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = UserLoginForm()
    return render(request=request, template_name="main/login.html", context={"login_form":form})


""" Multi-User Model SIGNUP VIEWS"""

def patient_registration(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = User.PATIENT
            user.save()
            return redirect('home')
    else:
        form = PatientRegistrationForm()
    return render(request, 'overlay-sign-up/index.html', {'form': form})

def doctor_registration(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = User.DOCTOR
            user.save()
            return redirect('home')
    else:
        form = DoctorRegistrationForm()
    return render(request, 'overlay-sign-up/index.html', {'form': form})

""" Multi-User Model LOGIN VIEWS"""
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid login credentials'        
    else:
        error_message = None
    return render(request, 'login.html', {'error_message': error_message})

