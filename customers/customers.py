from flask import render_template
from models import Customer

def customers():
    customers = Customer.query.all()
    return render_template("customers.html", customers=customers)
