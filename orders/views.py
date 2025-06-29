from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem
from cart.models import CartItem
from .forms import DesignOrderForm


def design_order(request):
    if request.method == 'POST':
        form = DesignOrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your design order har been submitted. We will get back to you shortly.')
            return redirect('portfolio')
    else:
        form = DesignOrderForm()
    return render(request, 'design_order.html', {'form': form})


@login_required
def order_list(request):
    """
    Shows a list of orders belonging to the logged-in user
    """
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})


@login_required
def checkout(request):
    """
    Convert the current cart into an Order and its OrderItems
    """
    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items.exists():
        messages.warning(request, "Your cart is empty.")
        return redirect('cart:cart_detail')

    if request.method == 'POST':
        # beräkna totalpriset
        total_price = sum(item.product.price * item.quantity for item in cart_items)

        # skapa order
        order = Order.object.create(
            user=request.user,
            total_price=total_price,
            status='pending'
        )

        # skapa orderrader
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
                price=item.product.price,
            )

        # Clear cart after checkout
        cart_items.delete()
        messages.success(request, f"Order #{order.id} created successfully!")
        return redirect('orders:order_complete' order_id=order.id)

    # för GET - visa sammanställning
    context = (
        'cart_items': cart_items,
        'total_price': sum(item.product.price * item.quantity for item in cart_items),
    )

    return render(request, 'orders/checkout.html', context)
