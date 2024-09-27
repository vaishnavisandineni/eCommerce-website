@app.route("/categories")
def categories():
    categories = Category.query.all()
    return render_template("categories.html", categories=categories)

@app.route("/category/<int:category_id>")
def category_products(category_id):
    category = Category.query.get_or_404(category_id)
    products = Product.query.join(ProductCategory).join(Category).filter(Category.id == category_id).all()
    return render_template("category_products.html", products=products, category=category)

@app.route("/search")
def search():
    query = request.args.get("q")
    products = Product.query.filter(Product.name.like("%" + query + "%") | Product.description.like("%" + query + "%")).all()
    return render_template("search_results.html", products=products, query=query)
