from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect  # Import redirect
from .forms import OrderForm
from carts.models import CartItem

def place_order(request):
    current_user = request.user

    # If the cart count is less than or equal to 0, redirect back to the store
    cart_item = CartItem.objects.filter(user=current_user)
    cart_count = cart_item.count()

    if cart_count <= 0:
        return redirect('store')

    return HttpResponse('ok')
 if request.method == 'POST':
form = OrderForm(request.POST)
if form.is_valid():
    date = Order()
    data.first_name  =  form.cleaned_data('first_name')
    data.last_name   = form.cleaned_data('last_name')
    data.phone  = form.cleaned_data('phone')
    data.email  = form.cleaned_data('email')
    data.address_line_1  = form.cleaned_data('address_line_1')
    data.address_line_2  = form.cleaned_data('address_line_2')
    data.country  = form.cleaned_data('country')
    data.state  = form.cleaned_data('state')
    data.city  = form.cleaned_data('city')
    data.order_note  = form.cleaned_data('order_note')
   data.order_total =
data.tax =