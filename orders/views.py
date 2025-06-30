from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem
from cart.models import CartItem
from .forms import DesignOrderForm
import stripe
from django.conf import settings


def design_order_view(request):
    if request.method == 'POST':
        form = DesignOrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your design order has been sent successfully!')
            return redirect('orders:design_order')
    else:
        form = DesignOrderForm()
    return render(request, 'orders/design_order.html', {'form': form})


@login_required
def order_list(request):
    """
    Shows a list of orders belonging to the logged-in user
    """
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})


stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def checkout(request):
    """
    Convert the current cart into an Order and its OrderItems
    Create an Stripe Checkout Session
    """
    db_items = CartItem.objects.filter(user=request.user)
    if not db_items.exists():
        messages.warning(request, "Your cart is empty.")
        return redirect('cart:cart_detail')
    
    line_items = []
    for item in db_items:
        line_items.append({
            'price_data': {
                'currency': 'sek',
                'unit_amount': int(item.product.price * 100),
                'product_data': {
                    'name': item.product.name,
                },
            },
            'quantity': item.quantity,
        })
    
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri('/orders/complete/success/'),
        cancel_url=request.build_absolute_uri('/cart/'),
        customer_email=request.user.email,
    )

    return redirect(checkout_session.url, code=303)


@login_required
def order_success(request):
    return render(request, 'orders/order_success.html')


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
