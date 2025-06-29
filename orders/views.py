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
    cart_items = []
    total_price = 0

    db_items = CartItem.objects.filter(user=request.user)

    if not db_items.exists():
        messages.warning(request, "Your cart is empty.")
        return redirect('cart:cart_detail')

    # build cart_items list with subtotal
    for item in db_items:
        subtotal = item.product.price * item.quantity
        cart_items.append({
            'product': item.product,
            'quantity': item.quantity,
            'subtotal': subtotal,
        })
        total_price += subtotal

    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            total_price=total_price,
            status='pending'
        )
        for item in db_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
            )
        db_items.delete()
        messages.success(request, f"Order #{order.id} created successfully!")
        return redirect('orders:order_complete', order_id=order.id)

    return render(request, 'orders/checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })


@login_required
def order_complete(request, order_id):
    """
    Show the confirmation after a completed order. 
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_complete.html', {'order': order})


@login_required
def order_history(request):
    """
    Show a list of previous orders for the logged-in user.
    """
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_history.html', {
        'orders': orders
    })


@login_required
def order_detail(request, order_id):
    """
    Show details of a specific order
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)

    # Lägg till subtotal i context
    subtotal_items = []
    for item in order.items.all():
        subtotal_items.append({
            "product": item.product,
            "price": item.price,
            "quantity": item.quantity,
            "subtotal": item.price * item.quantity,
        })

    context = {
        "order": order,
        "subtotal_items": subtotal_items,
    }
    return render(request, "orders/order_detail.html", context)
