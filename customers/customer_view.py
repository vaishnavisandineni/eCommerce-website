from flask import render_template
from models import Customer

def customer_view(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    return render_template("customer_view.html", customer=customer)
