import stripe

stripe.api_key = "YOUR_STRIPE_API_KEY"

def payment_gateway(request):
    try:
        # Get the payment details from the request
        payment_details = request.form

        # Create a Stripe payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=payment_details["amount"],
            currency="usd",
            payment_method_types=["card"],
        )

        # Return the payment intent client secret
        return payment_intent.client_secret
    except Exception as e:
        # Handle any errors that occur during payment processing
        print(f"Error processing payment: {e}")
        return None
