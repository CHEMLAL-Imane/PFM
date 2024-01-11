from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import OrderForm
from .models import Order
import datetime
from carts.models import CartItem
from carts.models import Cart
from carts.views import _cart_id


def payment(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    # Reste du code de la vue de paiement
    # ...

    context = {
        'order': order,
        # Autres contextes nécessaires
    }

    return render(request, 'orders/payments.html', context)

def place_order(request, total=0, quantity=0):
    current_user = request.user
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart)
    cart_count = cart_items.count()

    if cart_count <= 0:
        return redirect('store')

    grand_total = 0
    tax = 0

    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity

    tax = (2 * total) / 100
    grand_total = total + tax

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = current_user 
            order.order_total = grand_total
            order.tax = tax
            order.ip = request.META.get('REMOTE_ADDR')
            order.save()

            # Generate order number
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr, mt, dt)
            current_date = d.strftime("%Y%m%d")  # 20210305
            order_number = current_date + str(order.id)
            order.order_number = order_number
            order.save()

            return redirect('payments', order_number=order_number)
        else:
            return redirect('checkout')

    context = {
        'cart_items': cart_items,
        'total': total,
        'tax': tax,
        'grand_total': grand_total,
    }

    return render(request, 'orders/payments.html', context)
