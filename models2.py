class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('orders', lazy=True))
    products = db.relationship('Product', secondary='order_product', backref=db.backref('orders', lazy=True))
    total_price = db.Column(db.Float, nullable=False)
    shipping_address = db.Column(db.String(100), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class OrderProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, nullable=False)
