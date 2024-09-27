from app import app
from models import Product

@app.route("/products")
def product_list():
    products = Product.query.all()
    return render_template("product_list.html", products=products)

@app.route("/products/<int:product_id>")
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template("product_detail.html", product=product)
