from flask import render_template
from models import Order

def order_view(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template("order_view.html", order=order)
