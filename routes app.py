from admin_dashboard import admin_dashboard
from products import products
from product_edit import product_edit
from product_delete import product_delete
from orders import orders
from order_view import order_view
from customers import customers
from customer_view import customer_view

@app.route('/admin_dashboard')
def admin_dashboard():
    return admin_dashboard()

@app.route('/products')
def products():
    return products()

@app.route('/products/<int:product_id>/edit', methods=['GET', 'POST'])
def product_edit(product_id):
    return product_edit(product_id)

@app.route('/products/<int:product_id>/delete', methods=['POST'])
def product_delete(product_id):
    return product_delete(product_id)

@app.route('/orders')
def orders():
    return orders()

@app.route('/orders/<int:order_id>')
def order_view(order_id):
    return order_view(order_id)

@app.route('/customers')
def customers
