from cart.models import Cart


def cart_summary(request):
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        return {'cart_summary': cart}
    else:
        # return None
        return {'cart_summary': None}
