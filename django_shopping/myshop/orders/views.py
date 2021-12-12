from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

def order_create(reqeust):
    cart = Cart(reqeust)
    if reqeust.method == 'POST':
        form = OrderCreateForm(reqeust.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # clear the cart
            cart.clear()
            return render(reqeust,
                          'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(reqeust,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})