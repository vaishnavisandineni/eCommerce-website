// script.js

// Add event listener to add to cart button
document.addEventListener("DOMContentLoaded", function() {
    const addToCartButtons = document.querySelectorAll(".add-to-cart");
    addToCartButtons.forEach(button => {
        button.addEventListener("click", function() {
            const productId = button.dataset.productId;
            const quantity = button.dataset.quantity;
            addProductToCart(productId, quantity);
        });
    });
});

// Add product to cart function
function addProductToCart(productId, quantity) {
    const cart = JSON.parse(localStorage.getItem("cart")) || {};
    if (cart[productId]) {
        cart[productId] += parseInt(quantity);
    } else {
        cart[productId] = parseInt(quantity);
    }
    localStorage.setItem("cart", JSON.stringify(cart));
    updateCartCount();
}

// Update cart count function
function updateCartCount() {
    const cart = JSON.parse(localStorage.getItem("cart")) || {};
    const cartCount = Object.keys(cart).length;
    document.querySelector(".cart-count").textContent = cartCount;
}

// Remove product from cart function
function removeProductFromCart(productId) {
    const cart = JSON.parse(localStorage.getItem("cart")) || {};
    delete cart[productId];
    localStorage.setItem("cart", JSON.stringify(cart));
    updateCartCount();
}

// Update cart quantity function
function updateCartQuantity(productId, quantity) {
    const cart = JSON.parse(localStorage.getItem("cart")) || {};
    cart[productId] = parseInt(quantity);
    localStorage.setItem("cart", JSON.stringify(cart));
    updateCartCount();
}

// Checkout function
function checkout() {
    const cart = JSON.parse(localStorage.getItem("cart")) || {};
    const products = Object.keys(cart);
    const quantities = Object.values(cart);
    const total = products.reduce((acc, product, index) => {
        const price = parseFloat(document.querySelector(`#price-${product}`).textContent);
        return acc + price * quantities[index];
    }, 0);
    document.querySelector(".total").textContent = total.toFixed(2);
}

// Initialize cart count
updateCartCount();

// Add event listener to remove
