# Satchmo Stripe
This is a django app to help with stripe integration and satchmo.
Upgraded to work with Django 1.7+ and OpenCo cocom.

## To get working:

  * checkout to `satchmo_stripe` in your cocom folder
  * mv stripe.js to root static/js/stripe.js
  * add your `publish key` to static/js/stripe.js
  * `satchmo_stripe` should already be in  installed apps so no need to
    mess with that
  * Log into Django as admin and navigate to /settings. Add your
    `secret key` to the test secret key box under the Django stripe
    settings.

