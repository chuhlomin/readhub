from flask import Flask, render_template

app = Flask(__name__)
app.debug = False

@app.route('/')
def landing():

    books = [
        {'id': 1, 'title': 'Book 1'},
        {'id': 2, 'title': 'Book 2'},
        {'id': 3, 'title': 'Book 3'},
        {'id': 4, 'title': 'Book 4'},
    ]

    return render_template('landing.html', books=books)

@app.route('/book/<id>/')
def book(id):
    return render_template('book.html', id=id)

@app.route('/login/')
def login():
    return render_template('account/login.html')

@app.route('/register/')
def register():
    return render_template('account/register.html')

if __name__ == '__main__':
    app.run()
