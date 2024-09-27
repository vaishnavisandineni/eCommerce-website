from flask import render_template, request
from models import Product

def product_edit(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == "POST":
        product.name = request.form["name"]
        product.price = request.form["price"]
        db.session.commit()
        return redirect(url_for("products"))
    return render_template("product_edit.html", product=product)
