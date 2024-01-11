from ast import Param
from django.shortcuts import render,redirect

from carts.models import Cart, CartItem
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages,auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from carts.views import _cart_id
import requests




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
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                if is_cart_item_exists :
                    cart_item = CartItem.objects.filter(cart=cart)
                    product_variation = []
                    for item in cart_item :
                        variation = item.variations.all()
                        product_variation.append(list(variation))
                    
                    cart_item=CartItem.objects.filter(user = user)
                    ex_var_list =[]
                    id=[]
                    for item in cart_item :
                     existing_variation = item.variations.all()
                     ex_var_list.append(list(existing_variation))
                     id.append(item.id) 
                     
                    for pr in product_variation :
                        if pr in ex_var_list :
                            index = ex_var_list.index(pr)
                            item_id = id[index]
                            item = CartItem.objects.get(id=item_id)
                            item.quantity +=1
                            item.user = user
                            item.save()
                        else :
                            cart_item = CartItem.objects.filter(cart=cart)
                            for item in cart_item :
                                item.user = user
                                item.save()
                       
            except :
                pass
            auth.login(request,user)
            messages.success(request,'You are now logged in .')
            url =request.META.get('HTTP_REFERER')
        try:
          query = requests.utils.urlparse(url).query
          params = dict(x.split('=') for x in query.split('&'))
          if 'next' in params:
             nextPage = params['next']
             return redirect(nextPage)
             return redirect('dashboard')
        except:
         return redirect('dashboard')

    return render(request,'accounts/login.html')
@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request,'Your are logged out')
    return redirect('home')
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