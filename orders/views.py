import stripe
import stripe.error
from django.conf import settings
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin

from cart.models import CartItem

from .forms import DesignOrderForm
from .models import CompletedDesign, Order, OrderItem

stripe.api_key = settings.STRIPE_SECRET_KEY


@require_POST
def stripe_checkout(request, design_id):
    design = get_object_or_404(CompletedDesign, id=design_id)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'eur',
                'unit_amount': int(design.order.design_type.price * 100),
                'product_data': {
                    'name': f'Custom Design #{design.id}',
                },
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/orders/payment-success/'), OBS KOLLA OCH TA BORT IFALL DEN INTE BEHÖVS
        cancel_url=request.build_absolute_uri('/orders/payment-cancelled/'),
        metadata={
            'design_id': design.id
        }
    )

    return redirect(session.url, code=303)


@login_required
def pay_for_design(request, design_id):
    design = get_object_or_404(CompletedDesign, id=design_id)

    amount = int(design.order.design_type.price * 100)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'eur',
                'product_data': {
                    'name': f"Design Order #{design.order.id} - {design.order.design_type.name}",
                },
                'unit_amount': amount,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/orders/payment-success/') + f'?design_id={design_id}',
        cancel_url=request.build_absolute_uri('/orders/completed_designs/'),
        metadata={'design_id': str(design.id)},
    )
    return redirect(session.url, code=303)


@login_required
def payment_success(request):
    design_id = request.GET.get('design_id')
    if not design_id:
        messages.error(request, "Missing design ID.")
        return redirect('orders:my_completed_designs')

    design = get_object_or_404(CompletedDesign, id=design_id)

    # Only allow download if the user owns the design.
    if design.order.email != request.user.email:
        messages.error(request, "Access denied.")
        return redirect('orders:my_completed_designs')

    # Marking an paid (add the field below first!)
    design.paid = True
    design.save()

    # --- Confirmation email (Design order) ---
    #recipient = getattr(design.order, "email", None) or getattr(request.user, "email", None)
    #if recipient:
        #subject = "Your Artea Studio design – payment confirmed"
        #body = (
            #"Thank you for your payment.\n\n"
            #"Your completed design is now available for download on your account page.\n"
            #"If you did not make this purchase, please contact support."
        #)
        #try:
            #send_mail(
                #subject=subject,
                #message=body,
                #from_email=None,            # uses DEFAULT_FROM_EMAIL
                #recipient_list=[recipient],
                #fail_silently=True,         # safe in dev
            #)
        #except Exception:
            #pass
    # --- end email ---

    #messages.success(request, "Thank you for your payment! Your design is now available for download.")

    # Send confirmation email
    subject = "Thank you for your purchase at Artea Studio!"
    message = (
        f"Dear {request.user.username},\n\n"
        f"Your payment has been successfully processed and your design "
        f"is now available for download in your account.\n\n"
        f"Visit: https://www.artea.studio/orders/completed-designs/\n\n"
        f"Warm regards,\nArtea Studio Team"
    )
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [request.user.email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=True)

    return redirect('orders:my_completed_designs')


class PaymentSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'orders/payment_success.html'

    def get(self, request, *args, **kwargs):
        # Optional: clear cart session here if that´s your pattern
        # request.session["cart"] = {}

        # --- Confirmation email (Shop checkout) ---
        recipient = getattr(getattr(request, "user", None), "email", None)
        if recipient:
            try:
                send_mail(
                    subject="Thank you for your purchase at Artea Studio!",
                    message=(
                        f"Dear {request.user.username},\n\n"
                        f"Your payment has been successfully processed.\n"
                        f"You can view your orders/downloads in your account.\n\n"
                        f"Warm regards,\nArtea Studio Team"
                    ),
                    from_email=None,   # uses DEFAULT_FROM_EMAIL
                    recipient_list=[recipient],
                    fail_silently=False,  # sätt False under test
                )
            except Exception as e:
                print("EMAIL ERROR:", e)  # syns i terminalen/Heroku log

            #subject = "Your Artea Studio order – confirmation"
            #body = (
                #"Thank you for your purchase from Artea Studio.\n\n"
                #"This is a confirmation that your payment was successful (test environment).\n"
                #"If you did not make this purchase, please contact support."
            #)
            #try:
                #send_mail(
                    #subject=subject,
                    #message=body,
                    #from_email=None,
                    #recipient_list=[recipient],
                    #fail_silently=True,
                #)
            #except Exception:
                #pass
        # --- end email ---

        return super().get(request, *args, **kwargs)


class PaymentCancelledView(TemplateView):
    template_name = 'orders/payment_cancelled.html'


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
def my_completed_designs(request):
    user_email = request.user.email
    if not user_email:
        messages.error(request, "Your account has no email associated.")
        return redirect('home')

    designs = CompletedDesign.objects.filter(order__email=request.user.email)
    return render(request, 'orders/completed_designs.html', {'designs': designs})


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
                'currency': 'eur',
                'unit_amount': int(item.product.price * 100),
                'product_data': {
                    'name': item.product.title,
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
        metadata={
            'user_id': str(request.user.id)
        }
    )

    return redirect(checkout_session.url, code=303)


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    event = None

    # Choose the correct secret depending on the host address.
    if 'herokuapp.com' in request.get_host():
        webhook_secret = settings.STRIPE_WEBHOOK_SECRET_HEROKU
    else:
        webhook_secret = settings.STRIPE_WEBHOOK_SECRET_DOMAIN

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, webhook_secret
            )
        except ValueError:
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError:
            return HttpResponse(status=400)

    # If Stripe checkout completed.
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        metadata = session.get('metadata', {})
        design_id = metadata.get('design_id')

        if design_id:
            from .models import CompletedDesign
            try:
                design = CompletedDesign.objects.get(id=design_id)
                design.paid = True
                design.save()
            except CompletedDesign.DoesNotExist:
                pass
        else:
            # Continue as before with any order from shopping cart.
            handle_checkout_session(session)

    return HttpResponse(status=200)


def handle_checkout_session(session):
    """
    Creates an Order in database when Stripe confirmes payment.
    Also empties the user´s shopping cart.
    """
    from django.contrib.auth import get_user_model

    from cart.models import CartItem

    from .models import Order

    # We use metadata to send the user_id from checkout.
    user_id = session.get('metadata', {}).get('user_id')

    if not user_id:
        return

    User = get_user_model()
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return

    # Check if the user already has an open order.
    if Order.objects.filter(user=user, status='pending').exists():
        return  # Prevent duplication

    cart_items = CartItem.objects.filter(user=user)

    if not cart_items.exists():
        return

    # Create order
    order = Order.objects.create(
        user=user,
        total_price=session['amount_total'] / 100,  # Stripe totals in pennys
        status='paid'
    )

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    # Empty the shopping cart
    cart_items.delete()


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


@staff_member_required
def admin_design_list(request):
    """
    Admin view to list all completed desings
    """
    status = request.GET.get('status')
    if status == 'paid':
        designs = CompletedDesign.objects.filter(paid=True)
    elif status == 'unpaid':
        designs = CompletedDesign.objects.filter(paid=False)
    else:
        designs = CompletedDesign.objects.all()

    return render(request, 'orders/admin_design_list.html', {
        'designs': designs,
        'status': status,
    })


@staff_member_required
def mark_design_as_paid(request, design_id):
    """
    Allows an admin/staff user to manually mark a design as paid.
    """
    design = get_object_or_404(CompletedDesign, id=design_id)

    if design.paid:
        messages.info(request, "This design is already marked as paid.")
    else:
        design.paid = True
        design.save()
        messages.success(request, f"Design #{design.id} marked as paid.")

    return redirect('orders:admin_design_list')
