from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST

from cart.forms import CartAddProductForm
from cart.models import CartProduct, Cart
from shop.models import Product


class CartDetailView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        items = cart.cartproduct_set.all()
        cart.total_price = 0
        for item in items:
            item.update_quantity_form = CartAddProductForm(initial={
                'quantity': item.quantity,
                'override_quantity': True
            })
            item.total_price = item.quantity * item.product.price
            cart.total_price += item.total_price
        return render(request, 'cart/cart_detail.html', {'items': items, 'cart': cart})


class CartAddProductView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        user = request.user
        form = CartAddProductForm(request.POST)
        cart, created = Cart.objects.get_or_create(user=user)
        items = cart.cartproduct_set.all()
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            override_quantity = form.cleaned_data['override_quantity']
            if not any(item.product == product for item in items):  # wyrażenie generatorowe
                CartProduct.objects.create(product=product, cart=cart, quantity=0)
            cartproduct = CartProduct.objects.get(product=product, cart__user=user)
            if not override_quantity:
                cartproduct.quantity += quantity
            else:
                cartproduct.quantity = quantity
            cartproduct.save()
            return redirect('cart_detail')


class CartRemoveProductView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        user = request.user
        cart = Cart.objects.get(user=user)
        item = cart.cartproduct_set.filter(product_id=product_id)
        item.delete()
        return redirect('cart_detail')
