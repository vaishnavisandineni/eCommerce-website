from app import app
from cart import add_to_cart, view_cart, update_cart, remove_from_cart

@app.route("/cart")
def view_cart():
    return render_template("cart.html", cart=view_cart())

@app.route("/cart/<int:product_id>", methods=["POST"])
def update_cart(product_id):
    quantity = int(request.form["quantity"])
    update_cart(product_id, quantity)
    return redirect(url_for("view_cart"))

@app.route("/cart/<int:product_id>/remove", methods=["POST"])
def remove_from_cart(product_id):
    remove_from_cart(product_id)
    return redirect(url_for("view_cart"))
