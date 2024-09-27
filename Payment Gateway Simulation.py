from flask import request, redirect, url_for

def payment_gateway():
    # Simulate payment gateway
    payment_status = "success"
    if payment_status == "success":
        # Update order status
        order = Order.query.get_or_404(request.args.get("order_id"))
        order.status = "paid"
        db.session.commit()
        flash("Payment successful!")
        return redirect(url_for("home"))
    else:
        flash("Payment failed!")
        return redirect(url_for("checkout"))
