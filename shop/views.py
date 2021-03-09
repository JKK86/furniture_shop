from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from shop.forms import RegistrationForm
from shop.models import Product, Category


class IndexView(View):
    def get(self, request):
        return render(request, 'shop/base.html')


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
        products = Product.objects.filter(stock__gt=0)
        categories = Category.objects.all()
        category = None
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'shop/product_list.html', {
            'products': products, 'categories': categories, 'category': category
        })


class ProductDetailView(View):
    def get(self, request, id, slug):
        pass
