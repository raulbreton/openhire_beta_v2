from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from employers.models import EmployerProfile

def register_user(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        account_type = request.POST.get('account_type')

        if form.is_valid() and account_type in ['Candidato', 'Empleador']:
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            user = authenticate(username=email, password=password)
            login(request, user)

            if account_type == 'Empleador':
                form.instance.is_employer = True
                form.instance.is_candidate = False
                form.save()
                EmployerProfile.objects.create(user=user) #Create automatically the Employer Profile
                #return redirect('#')
            elif account_type == 'Candidato':
                form.instance.is_employer = False
                form.instance.is_candidate = True
                form.save()
                #return redirect('#')
        else:
            return render(request, "register.html", {'form': form})

    return render(request, "register.html", {'form': form})

def login_user(request):
    if request.user.is_authenticated:
        logout(request)

    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_employer == True:
                return redirect('http://127.0.0.1:8000/admin/')
            else:
                return redirect('http://127.0.0.1:8000/admin/')
        else:
            return redirect('login')

    return render(request, "login.html", {})


def logout_user(request):
    user = request.user
    logout(request)
    
    if user.is_employer == True:
        return redirect('http://127.0.0.1:8000/admin/')
    else:
        return redirect('http://127.0.0.1:8000/admin/')