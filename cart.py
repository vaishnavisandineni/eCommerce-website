from flask import session

cart = {}

def add_to_cart(product_id, quantity):
    if product_id in cart:
        cart[product_id]["quantity"] += quantity
    else:
        cart[product_id] = {"quantity": quantity}

def view_cart():
    return cart

def update_cart(product_id, quantity):
    if product_id in cart:
        cart[product_id]["quantity"] = quantity

def remove_from_cart(product_id):
    if product_id in cart:
        del cart[product_id]
