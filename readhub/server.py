from flask import render_template, flash, redirect, url_for
from readhub import app
from readhub import db
from forms import RegistrationForm
from models import User

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

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        # todo check for error

        flash('Account created! %s' % user.id)
        return redirect(url_for('landing'))

    return render_template('account/register.html', form=form)

#  Some useful headers to set to beef up the robustness of the app
# https://www.owasp.org/index.php/List_of_useful_HTTP_headers
@app.after_request
def after_request(response):
    response.headers.add('Content-Security-Policy', "default-src 'self' 'unsafe-inline' data:")
    response.headers.add('X-Frame-Options', 'deny')
    response.headers.add('X-Content-Type-Options', 'nosniff')
    response.headers.add('X-XSS-Protection', '1; mode=block')
    return response
