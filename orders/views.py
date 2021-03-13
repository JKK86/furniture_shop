from django.shortcuts import render, redirect

from django.views import View

from cart.models import Cart
from orders.forms import DeliveryTypeForm, DeliveryAddressForm
from orders.models import ODBIOR, Order, OrderItem, DeliveryAddress, KURIER


class OrderCreateView(View):
    def get(self, request):
        form_delivery_type = DeliveryTypeForm(initial={'delivery_type': KURIER})
        form_delivery_address = DeliveryAddressForm()
        user = request.user
        cart = Cart.objects.get(user=user)
        items = cart.cartproduct_set.all()
        for item in items:
            item.total_price = item.quantity * item.product.price

        return render(request, 'orders/order_create.html', {
            'form_delivery_type': form_delivery_type,
            'form_delivery_address': form_delivery_address,
            'cart': cart,
            'items': items
        })

    def post(self, request):
        user = request.user
        cart = Cart.objects.get(user=user)
        items = cart.cartproduct_set.all()
        form_delivery_type = DeliveryTypeForm(request.POST)
        form_delivery_address = DeliveryAddressForm(request.POST)
        if form_delivery_type.is_valid():
            delivery = form_delivery_type.cleaned_data['delivery_type']
            if delivery == "OD":
                order = Order.objects.create(
                    user=user,
                    delivery=delivery,
                    delivery_address=None
                )
            else:
                form_delivery_address = DeliveryAddressForm(request.POST)
                if form_delivery_address.is_valid():
                    address = form_delivery_address.cleaned_data['address']
                    postal_code = form_delivery_address.cleaned_data['postal_code']
                    city = form_delivery_address.cleaned_data['city']

                    delivery_address = DeliveryAddress.objects.create(
                        user=user,
                        address=address,
                        postal_code=postal_code,
                        city=city
                    )
                    order = Order.objects.create(
                        user=user,
                        delivery=delivery,
                        delivery_address=delivery_address
                    )
                else:
                    return render(request, 'orders/order_create.html', {
                        'form_delivery_type': form_delivery_type,
                        'form_delivery_address': form_delivery_address,
                        'cart': cart,
                        'items': items
                    })
            for item in items:
                OrderItem.objects.create(
                    product=item.product,
                    order=order,
                    quantity=item.quantity,
                    price=item.product.price)
                item.product.stock -= item.quantity
                item.product.save()
            items.delete()
            return render(request, 'orders/order_created.html', {'order': order})
        else:
            return render(request, 'orders/order_create.html', {
                'form_delivery_type': form_delivery_type,
                'form_delivery_address': form_delivery_address,
                'cart': cart,
                'items': items
            })
