from flask import render_template
from models import Product

def products():
    products = Product.query.all()
    return render_template("products.html", products=products)
