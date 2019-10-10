import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, render_template, request, redirect, url_for

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Contractor')
client = MongoClient(host=host)
db = client.get_default_database()
guitars = db.guitar
# cart_items = db.cart_items
app = Flask(__name__)

@app.route('/')
def guitars_index():
    """Show all guitars."""
    return render_template('guitars_index.html', guitars=guitars.find())

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/guitars/new')
def guitars_new():
    """Create a custom guitar store."""
    return render_template('guitars_new.html', guitar={}, title='Discount Guitars')

@app.route('/guitars', methods=['POST'])
def guitars_submit():
    guitar = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'jpgs': request.form.get('jpgs'),
        'type_of_guitar': request.form.get('types')
    }
    guitars.insert_one(guitar)
    return redirect(url_for('guitars_index'))

@app.route('/guitars/<guitar_id>/edit', methods=['POST'])
def guitars_edit(guitar_id):
    """Show the edit form for a guitar."""
    guitar = guitars.find_one({'_id': ObjectId(guitar_id)})
    return render_template('guitars_edit.html', guitar=guitar, title='Edit guitar')

@app.route('/guitars/<guitar_id>/save_edit', methods=['POST'])
def save_edit(guitar_id):
    """Update New Guitar"""
    guitar = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'jpgs': request.form.get('jpgs'),
        'type_of_guitar': request.form.get('types')
    }
    guitars.update_one({'_id': ObjectId(guitar_id)},{"$set":guitar})
    return redirect(url_for('guitars_index'))

@app.route('/guitars/<guitar_id>/delete', methods=['POST'])
def guitars_delete(guitar_id):
    """Delete one guitar."""
    guitars.delete_one({'_id': ObjectId(guitar_id)})
    return redirect(url_for('guitars_index'))

@app.route('/acoustic_guitars/show')
def acoustic_guitars():
    """Display Acoustic Guitars"""
    return  render_template('acoustic_guitars.html')

@app.route('/electric_guitars/show')
def electric_guitars():
     """Display Electric Guitars"""
     return render_template('electric_guitars.html')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))

# @app.route('/checkout_cart', methods =['POST'])
# def checkout_cart():
#     new_cart_item = {
#     "make_model": request.form.get("make_model"),
#     "type": request.form.get("type"),
#     "cost": request.form.get("cost")
#     }
#     cart_items.insert_one(new_cart_item)
#     """Checkout items to cart"""
#     return render_template('checkout_cart.html', cart_items=cart_items.find())
