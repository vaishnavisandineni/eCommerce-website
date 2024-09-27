from app import app
from models import Order, OrderProduct

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    cart = view_cart()
    if not cart:
        flash("Your cart is empty!")
        return redirect(url_for("home"))
    order = Order(user_id=current_user.id, total_price=sum([product.price * quantity for product, quantity in cart.items()]))
    db.session.add(order)
    db.session.commit()
    for product_id, quantity in cart.items():
        order_product = OrderProduct(order_id=order.id, product_id=product_id, quantity=quantity)
        db.session.add(order_product)
    db.session.commit()
    flash("Your order has been placed successfully!")
    return redirect(url_for("home"))

@app.route("/my_orders")
def my_orders():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    orders = current_user.orders.all()
    return render_template("my_orders.html", orders=orders)
