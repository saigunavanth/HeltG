from django.shortcuts import render,redirect
from accounts.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm


def base(request):
	return render(request,'accounts/base.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request,user)
            return redirect('main1')
        else:
        	print('error')
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})



def registration(request):
    form = RegistrationForm(request.POST)
    form1 = RegistrationForm1(request.POST)
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        
        form1 = RegistrationForm(request.POST)
        print(form)
        if form.is_valid() and form1.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('main1')
        else:
            print("error")
    else:
        print("method error")
    return render(request,"accounts/registration.html",{'form':form,'form1':form1})



