from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import CartItem


def cart_detail(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart/cart_detail.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:cart_detail')
