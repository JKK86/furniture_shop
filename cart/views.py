from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User

from cart.forms import CartAddProductForm, CartSetColorForm
from cart.models import CartProduct, Cart, NATURALNY
from coupon.forms import AddCouponForm
from orders.forms import DeliveryTypeForm
from orders.models import ODBIOR
from shop.models import Product


class CartDetailView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        items = cart.cartproduct_set.all()
        form_coupon = AddCouponForm()
        cart.total_price = 0
        for item in items:
            item.update_quantity_form = CartAddProductForm(initial={
                'quantity': item.quantity,
                'override_quantity': True
            })
            item.total_price = item.quantity * item.product.price
            cart.total_price += item.total_price
        return render(request, 'cart/cart_detail.html', {'items': items, 'cart': cart, 'form_coupon': form_coupon})


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
            if cartproduct.quantity > product.stock:
                cartproduct.quantity = product.stock
                messages.warning(request, "Ze względu na dostępność, liczba zamówionych produktów została ograniczona")
            cartproduct.save()
            return redirect('cart_detail')


class CartRemoveProductView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        user = request.user
        cart = Cart.objects.get(user=user)
        item = cart.cartproduct_set.filter(product_id=product_id)
        item.delete()
        return redirect('cart_detail')


class CartSetProductColorView(LoginRequiredMixin, View):
    def get(self, request, product_id):
        form = CartSetColorForm()
        return render(request, 'shop/set_color.html', {'form': form})

    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        user = request.user
        form = CartSetColorForm(request.POST)
        if form.is_valid():
            color = form.cleaned_data['color']
            cartproduct = CartProduct.objects.get(product=product, cart__user=user)
            cartproduct.color = color
            cartproduct.save()
            return redirect('cart_detail')
