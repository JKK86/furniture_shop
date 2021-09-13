"""sklep_meblowy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from shop import views
from cart import views as cart_views
from orders import views as orders_views
from account import views as account_views
from coupon import views as coupon_views
from payment import views as payment_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('registration/', account_views.RegistrationView.as_view(), name='registration'),

    path('account/', account_views.MyAccountView.as_view(), name='my_account'),
    path('account/edit_profile/', account_views.EditProfileView.as_view(), name='edit_profile'),


    path('cart/', cart_views.CartDetailView.as_view(), name='cart_detail'),
    path('cart/add/<int:product_id>/', cart_views.CartAddProductView.as_view(), name='cart_add'),
    path('cart/remove/<int:product_id>/', cart_views.CartRemoveProductView.as_view(), name='cart_remove'),
    path('cart/set_color/<int:product_id>/', cart_views.CartSetProductColorView.as_view(), name='set_color'),

    path('orders/create/', orders_views.OrderCreateView.as_view(), name='order_create'),

    path('coupon/apply/', coupon_views.ApplyCouponView.as_view(), name='apply_coupon'),

    path('payment/process/', payment_views.PaymentView.as_view(), name='payment_process'),
    path('payment/done/', payment_views.payment_done, name='payment_done'),
    path('payment/cancelled/', payment_views.payment_cancelled, name='payment_cancelled'),

    path('customize_product/', views.CustomizeProductView.as_view(), name='customize_product'),
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<slug:category_slug>/', views.ProductListView.as_view(), name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('search', views.SearchProductView.as_view(), name='product_search'),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)