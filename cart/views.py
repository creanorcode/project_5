from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import CartItem


def cart_detail(request):
    """
    Display all CartItems currently in the cart
    """
    cart_items =[]
    total_price = 0

    if request.user.is_authenticated:
        # Authenticated user - fetch from DB
        items = CartItem.objects.filter(user=request.user)
        for item in items:
            cart_items.append({
                'product': item.product,
                'quantity': item.quantity,
                'subtotal': item.product.price * item.quantity,
            })
            total_price += item.product.price * item.quantity
    else:
        # Anonumous user - fetch from session
        session_cart = request.session.get('cart', {})
        for product_id, quantity in session_cart.items():
            product = get_object_or_404(Product, id=product_id)
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': product.price * quantity,
            })
            total_price += product.price * quantity

    return render(request, 'cart/cart_detail.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })


def add_to_cart(request, product_id):
    """
    Add a product to the cart, or increase quantity if it already exists.
    """
    if not request.user.is_authenticated:
        return redirect('login')
    
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1}
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
