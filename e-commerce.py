from flask import Flask, render_template, request
app = Flask(__name__)
products = [{'id': 1, 'name': 'Shirt', 'price': 25}, {'id': 2, 'name': 'Pants', 'price': 40}]
cart = []
@app.route('/')
def home():
    return render_template('index.html', products=products)
@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    cart.append(products[product_id - 1])
    return render_template('cart.html', cart=cart)
if __name__ == '__main__':
    app.run(debug=True)
