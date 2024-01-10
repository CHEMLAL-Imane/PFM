from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages,auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required





# Create your views here.
def register(request):
    if request.method =='POST' :
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data[' first_name']
            email = form.cleaned_data['email']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.save()
            messages.success(request,'Registration successful')
            return redirect('register')
    else:
        form = RegistrationForm()

    context ={
        'form' : form,
    }
   
    return render(request,'accounts/register.html', context)

def login (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        
        if user is not None :
            auth.login(request,user)
            messages.success(request,'You are now logged in .')
            return redirect('dashboard')
        else :
            messages.error(request,'Invalid informations . Try again')
            return redirect('login')
    return render(request,'accounts/login.html')

@login_required(login_url = 'login')

def logout(request):
    auth.logout(request)
    messages.success(request,'Your are logged out')
    return redirect('login')
def activate(request):
    return
@login_required(login_url = 'login')
def dashboard(request):
    return render(request,'accounts/dashboard.html')


def forgotPassword(request):
    if request.method == 'POST' :
        username = request.POST['username']
        if Account.objects.filter(username=username).exists():
            user = Account.object.get(username__exact=username)
            
        else :
            messages.error(request,'Account does not exist !')
    return render(request ,'accounts/forgotPassword.html')