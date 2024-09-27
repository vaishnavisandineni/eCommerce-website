from flask import render_template
from models import Order

def orders():
    orders = Order.query.all()
    return render_template("orders.html", orders=orders)
