from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

"""def register_user(request):
    form = SignUpForm
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            is_employer = form.cleaned_data['is_employer']
            is_candidate = form.cleaned_data['is_candidate']
            #Log in user
            user = authenticate(username=email,password=password)
            login(request,user)
            #messages.success(request, 'Te has registrado con éxito!')
            
            if is_employer == True:
                print("Employers")
                #return redirect('employers_home')
            else:
                print("Candidates")
                #return redirect('candidates_home')
        else:
            return render(request, "register.html", {'form':form})
    return render(request, "register.html", {'form':form})"""
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
                #messages.success(request, 'Te has registrado como empleador con éxito!')
                #return redirect('employers_home')
            elif account_type == 'Candidato':
                form.instance.is_employer = False
                form.instance.is_candidate = True
                form.save()
                #messages.success(request, 'Te has registrado como candidato con éxito!')
                #return redirect('candidates_home')
        else:
            return render(request, "register.html", {'form': form})

    return render(request, "register.html", {'form': form})
