from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, LoginForm
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
        form = LoginForm(request.POST)
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if not user.objects.filter(username=username).exists():
            form.add_error('email', "Direccion incorrecta. Porfavor intenta de nuevo.")
        elif not user.objects.filter(password=password).exists():
            form.add_error(None, "Contraseña incorrecta. Porfavor intenta de nuevo.")
        else:
            form.add_error(None, "Correo y/o Contraseña invalido. Porfavor intenta de nuevo.")

        login(request, user)

        if user.is_employer == True:
            return redirect('http://127.0.0.1:8000/admin/')
        else:
            return redirect('http://127.0.0.1:8000/admin/')

    return render(request, "login.html", {})

def login_user(request):
    if request.user.is_authenticated:
        logout(request)

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)

                if user.is_employer:
                    return redirect('http://127.0.0.1:8000/admin/')
                
                else:
                    return redirect('http://127.0.0.1:8000/admin/')
            else:
                form.add_error("email", "Credenciales invalidas")
                form.add_error("password", "Credenciales invalidas")
                return render(request, "login.html", {'form': form})
    else:
        form = LoginForm()
        
    return render(request, "login.html", {'form': form})