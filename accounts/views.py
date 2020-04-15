from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages
from accounts.forms import LoginForm, RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required    
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))
    
def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST) # populate the form from what the user has keyed in
        if login_form.is_valid():
            # attempt to check the username and password is valid
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            messages.success(request, "You have successfully logged in")
            if user:
                # log in the user
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Invalid username or password")
                return render(request, 'login.html', {
                  'form':login_form
                })

    else:
        login_form = LoginForm()
        return render(request, 'login.html', {
            'form':login_form
        })

def register(request):
    User = get_user_model()
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        # NEW CODE STARTS HERE
        if register_form.is_valid():
            
            #1 create the user
            register_form.save()

            #2 check if the user has been created properly
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                #3 if the user has been created successful, attempt to login
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, "Unable to register your account at this time")
            return redirect(reverse('index'))
        #NEW CODE ENDS HERE
        else:
            return render(request, 'register.html', {
                'form':register_form
            })
    else:
        register_form = RegistrationForm()
        return render(request, 'register.html',{
                'form' : register_form
        })