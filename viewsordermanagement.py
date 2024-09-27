@app.route("/order/<int:order_id>")
def order_detail(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template("order_detail.html", order=order)
