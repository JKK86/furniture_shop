from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from cart.forms import CartAddProductForm
from orders.models import Order, DeliveryAddress
from shop.forms import CustomizedProductForm
from shop.models import Product, Category, CustomizedProduct, Wood


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


class CustomizeProductView(LoginRequiredMixin, View):
    def get(self, request):
        form = CustomizedProductForm()
        return render(request, "shop/customize_product_form.html", {'form': form})

    def post(self, request):
        form = CustomizedProductForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            customized_product = form.save(commit=False)
            user = request.user
            customized_product.user = user
            customized_product.save()
            subject = f"Zlecenie na wykonanie projektu na zamowienie"
            subject = subject[0][0]
            message = f"""Użytkownik {user.first_name} {user.last_name}, {user.email} 
przesyła zlecenie na wykonanie produktu na zamówienie.
Nazwa projektu: {customized_product.name}.
Szczegóły dotyczące projektu znajdują się na stronie panelu administracyjnego, 
w zakładce 'Produkty na zamówienie'.
Czas na odpowiedź - 3 dni robocze
"""
            email_from = "shop_orders@local.com"
            admins = User.objects.filter(is_staff=True)
            email_to = [admin.email for admin in admins]
            send_mail(subject, message, email_from, email_to, fail_silently=False)
            ctx = {"customized_product": customized_product}
            return render(request, "shop/customize_product_confirmation.html", ctx)
