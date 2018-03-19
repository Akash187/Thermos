from flask import Flask, render_template, request,url_for, redirect
from datetime import datetime

from logging import DEBUG

app = Flask(__name__)
app.logger.setLevel(DEBUG)

bookmarks = []

def store_bookmark(url):
    bookmarks.append(dict(
        url = url,
        user = "Akash",
        date = datetime.utcnow()
    ))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Text passed from view to template", text="Text passed from view to template", user = User("Akash Kumar", "Seth"))

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmark(url)
        app.logger.debug('stored url: ' + url)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def initials(self):
        return "{} {}".format(self.firstname[0], self.lastname[0])

if __name__ == "__main__":
    app.run(debug=True)