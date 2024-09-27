from flask import render_template

def order_confirmation(request):
    try:
        # Get the order details from the request
        order_details = request.form

        # Render the order confirmation template
        return render_template("order_confirmation.html", order_details=order_details)
    except Exception as e:
        # Handle any errors that occur during order confirmation
        print(f"Error confirming order: {e}")
        return None
