from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from cart.forms import CartAddProductForm
from orders.models import Order, DeliveryAddress
from shop.forms import RegistrationForm
from shop.models import Product, Category


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
        return super().form_valid(form)


class ProductListView(View):
    def get(self, request, category_slug=None):
        products_list = Product.objects.filter(stock__gt=0)
        categories = Category.objects.all()
        category = None
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products_list = products_list.filter(category=category)
        paginator = Paginator(products_list, 30)
        page = request.GET.get('page', 1)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        return render(request, 'shop/product_list.html', {
            'products': products, 'categories': categories, 'category': category
        })


class ProductDetailView(View):
    def get(self, request, id, slug):
        product = get_object_or_404(Product, pk=id, slug=slug)
        if product.stock == 0:
            product.available = "Produkt niedostępny"
        else:
            product.available = "Produkt dostępny"
        form = CartAddProductForm()
        return render(request, 'shop/product_detail.html', {'product': product, 'form': form})


class SearchProductView(View):
    def get(self, request):
        search_name = request.GET.get('search_product')
        products_list = Product.objects.filter(name__icontains=search_name)
        categories = Category.objects.all()
        category = None
        paginator = Paginator(products_list, 30)
        page = request.GET.get('page', 1)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        return render(request, 'shop/product_list.html', {
            'products': products, 'categories': categories, 'category': category
        })


class MyAccountView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        orders = Order.objects.filter(user=user)
        for order in orders:
            order.total_price = sum([item.quantity * item.product.price for item in order.orderitem_set.all()])
        delivery_addresses = DeliveryAddress.objects.filter(user=user)
        return render(request, "shop/my_account.html", {'orders': orders, 'delivery_addresses': delivery_addresses})
