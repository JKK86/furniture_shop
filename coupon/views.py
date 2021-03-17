from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View

from cart.models import Cart
from coupon.forms import AddCouponForm
from coupon.models import Coupon


class ApplyCouponView(LoginRequiredMixin, View):
    def post(self, request):
        form = AddCouponForm(request.POST)
        now = timezone.now()
        user = request.user
        cart = Cart.objects.get(user=user)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                coupon = Coupon.objects.get(code=code, valid_from__lte=now, valid_to__gte=now, active=True)
                cart.coupon = coupon
            except Coupon.DoesNotExist:
                cart.coupon = None
                messages.error(request, "Podany kupon rabatowy jest nieprawidłowy albo nie jest obecnie aktywny")
            cart.save()
        return redirect('cart_detail')
