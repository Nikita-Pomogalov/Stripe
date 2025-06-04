from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.conf import settings
import requests
from urllib3 import request
from .models import Item, Order
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def detail(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'item.html', {
        'item': item,
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
    })

def create_session_for_item(request, id):
    print("Stripe Key:", settings.STRIPE_SECRET_KEY)
    item = get_object_or_404(Item, id=id)
    session = stripe.checkout.Session.create(
        payment_method_types = ['card'],
        line_items = [{
            'price_data':{
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price * 100,
            },
            'quantity': 1,
        }],
        mode = 'payment',
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri('/cancel/'),
    )
    return JsonResponse({'id': session.id})

def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    return render(request, 'order.html', {
        'order': order,
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
    })

def create_session_for_order(request, id):
    order = get_object_or_404(Order, id=id)
    line_items = []
    for item in order.items.all():
        line_items.append({
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price * 100,
            },
            'quantity': 1,
        })
    discounts = []
    if order.discount:
        discounts.append({
            'coupon': order.discount.stripe_coupon_id
        })
    session =  stripe.checkout.Session.create(
        payment_method_types = ['card'],
        line_items = line_items,
        mode = 'payment',
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri('/cancel/'),
    )

    return JsonResponse({'id': session.id})

