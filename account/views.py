from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from account.forms import RegistrationForm, EditProfileForm
from orders.models import Order, DeliveryAddress


class RegistrationView(FormView):
    template_name = 'registration/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        User.objects.create_user(
            username=form.cleaned_data['username'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email']
        )
        messages.success(self.request, "Użytkownik został pomyślnie zarejestrowany")
        return super().form_valid(form)


class MyAccountView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        orders = Order.objects.filter(user=user)
        # for order in orders:
        #     order.total_price = sum([item.quantity * item.product.price for item in order.orderitem_set.all()])
        delivery_addresses = DeliveryAddress.objects.filter(user=user)
        return render(request, "account/my_account.html", {'orders': orders, 'delivery_addresses': delivery_addresses})


class EditProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = EditProfileForm(instance=request.user)
        return render(request, 'account/edit_profile.html', {'form': form})

    def post(self, request):
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('my_account')
