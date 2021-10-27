from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """ A view to show the checkout """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Oooops there's nothing in your bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Jp99VLo6obsE5gGt5YzhCafirSnatf449hX8mQVAEnKDEIfBpHBxd7gniwmULTB4ZKh68dozoCEiSlLyTxBO4Hn002yf6yYSC',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
