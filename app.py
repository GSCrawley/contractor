import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, render_template, request, redirect, url_for

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Contractor')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
guitars = db.guitars
# comments = db.comments
app = Flask(__name__)

@app.route('/')
def guitars_index():
    """Show all guitars."""
    return render_template('guitars_index.html', guitars=guitars)

# @app.route('/guitars/new')
# def guitars_new():
#     """Create a custom guitar store."""
#     return render_template('guitars_new.html', guitar={}, title='Custom Guitars')
#
# @app.route()
