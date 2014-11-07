from flask import render_template, flash, redirect, url_for
from readhub import app
from readhub import db
from forms import RegistrationForm, LoginForm, BookAddForm
from models import User
from flask.ext.login import LoginManager, login_user, logout_user

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


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
def book_view(id):
    return render_template('book/view.html', id=id)

@app.route('/book/add/', methods=['GET', 'POST'])
def book_add():
    form = BookAddForm()
    return render_template('book/add.html', form=form)

@app.route('/login/', methods=['GET', 'POST'])
def auth_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if user.valid_password(form.password.data):
                flash('Welcome! %s' % user.email)
                # session['user_id'] = user.id
                login_user(user)
                return redirect(url_for('landing'))
            else:
                flash('Fooo!')

    return render_template('account/login.html', form=form)


@app.route('/logout/')
def auth_logout():
    logout_user()
    return redirect(url_for('landing'))


@app.route('/register/', methods=['GET', 'POST'])
def auth_register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        # todo check for error

        flash('Account created! %s' % user.id)
        return redirect(url_for('landing'))

    return render_template('account/register.html', form=form)


# Some useful headers to set to beef up the robustness of the app
# https://www.owasp.org/index.php/List_of_useful_HTTP_headers
@app.after_request
def after_request(response):
    response.headers.add('Content-Security-Policy', "default-src 'self' 'unsafe-inline' data:")
    response.headers.add('X-Frame-Options', 'deny')
    response.headers.add('X-Content-Type-Options', 'nosniff')
    response.headers.add('X-XSS-Protection', '1; mode=block')
    return response
