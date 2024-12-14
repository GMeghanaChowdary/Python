import os
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def image_gallery():
    image_folder = 'images/'
    images = os.listdir(image_folder)
    return render_template('gallery.html', images=images)
