from flask import Flask, render_template, request
app = Flask(__name__)
posts = []
@app.route('/')
def home():
    return render_template('index.html', posts=posts)
@app.route('/add', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    posts.append({'title': title, 'content': content})
    return render_template('index.html', posts=posts)
if __name__ == '__main__':
    app.run(debug=True)
