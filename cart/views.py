from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import CartItem
from django.utils import timezone


def cart_detail(request):
    """
    Display all CartItems currently in the cart
    """
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart/cart_detail.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })


def add_to_cart(request, product_id):
    """
    Add a product to the cart, or increase quantity if it already exists.
    """
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        product=product,
        defaults={
            'quantity': 1,
            'created_at': timezone.now()
        }
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart:cart_detail')


def remove_from_cart(request, item_id):
    """
    Remove a specific CartItem from the cart by ID.
    """
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart:cart_detail')


def update_cart(request, item_id):
    """
    Update quantity for a CartItem.
    """
    item = get_object_or_404(CartItem, id=item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        item.quantity = quantity
        item.save()
    return redirect('cart:cart_detail')
