from django.shortcuts import render, get_object_or_404, redirect
import braintree
from django.views import View

from orders.models import Order
from sklep_meblowy import settings

gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)


class PaymentView(View):
    def get(self, request):
        # user = request.user
        order_id = request.session.get('order_id')
        order = get_object_or_404(Order, pk=order_id)
        client_token = gateway.client_token.generate()
        return render(request, 'payment/payment_process.html', {'client_token': client_token, 'order': order})

    def post(self, request):
        order_id = request.session.get('order_id')
        order = get_object_or_404(Order, pk=order_id)
        nonce = request.POST.get('payment_method_nonce', None)
        result = gateway.transaction.sale({
            'amount': f'{order.get_total_cost()}',
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
        if result.is_success:
            order.paid = True
            order.braintree_id = result.transaction.id
            order.save()
            return redirect('payment_done')
        else:
            return redirect('payment_cancelled')


def payment_done(request):
    return render(request, 'payment/payment_done.html')


def payment_cancelled(request):
    return render(request, 'payment/payment_cancelled.html')




