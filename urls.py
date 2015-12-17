from django.conf.urls import patterns
from satchmo_store.shop.satchmo_settings import get_satchmo_setting

ssl = get_satchmo_setting('SSL', default_value=False)

urlpatterns = patterns('',
    (r'^$', 'satchmo_stripe.views.pay_ship_info', {'SSL':ssl}, 'SATCHMO_STRIPE_satchmo_checkout-step2'),
    (r'^confirm/$','satchmo_stripe.views.confirm_info', {'SSL':ssl}, 'SATCHMO_STRIPE_satchmo_checkout-step3'),
    (r'^success/$', 'payment.views.checkout.success', {'SSL':ssl}, 'SATCHMO_STRIPE_checkout-success'),
)
