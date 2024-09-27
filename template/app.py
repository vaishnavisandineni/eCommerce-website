from flask import request, render_template
from payment_gateway import payment_gateway
from order_confirmation import order_confirmation
from email_notification import email_notification

@app.route("/payment", methods=["POST"])
def payment():
    client_secret = payment_gateway(request)
    return render_template("payment.html", client_secret=client_secret)

@app.route("/order_confirmation", methods=["POST"])
def order_confirmation():
    order_details = order_confirmation(request)
    return render_template("order_confirmation.html", order_details=order_details)

@app.route("/email_notification", methods=["POST"])
def email_notification():
    email_details = email_notification(request)
    return email_details
