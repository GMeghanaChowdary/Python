from flask import Flask, request
import os
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def home():
    return '<h1>Upload File</h1><form method="POST" enctype="multipart/form-data"><input type="file" name="file"><input type="submit"></form>'
@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return 'File uploaded successfully'
if __name__ == '__main__':
    app.run(debug=True)
