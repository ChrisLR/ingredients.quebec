import pymodm
from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

import models
from forms.login import LoginForm


def connect_to_mongodb():
    """
    Connects to the database using pymodm
    """
    # TODO The connection string must be imported from somewhere
    # TODO We can use an ini file or environment variables.
    connection_uri = "mongodb://localhost:27017/ingredientsquebec"
    pymodm.connect(connection_uri, alias="default")


# Flask Settings
application = Flask(__name__)
Bootstrap(application)

# Set the secret key to some random bytes. Keep this really secret!
dev_secret_key = b'r.`se#2:X@r<N8N'
application.secret_key = dev_secret_key
application.config.from_pyfile('config.py', silent=True)


def prepare_login_manager(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    return login_manager


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/apropos')
def apropos():
    return render_template('apropos.html')


@application.route('/malteries')
def malteries():
    result_malteries = models.Malterie.objects.all()
    return render_template('malteries.html', malteries=result_malteries)


@application.route('/houblonnieres')
def houblonnieres():
    result_houblonnieres = models.Houblonniere.objects.all()
    return render_template('houblonnieres.html', houblonnieres=result_houblonnieres)


@application.route('/levuriers')
def levuriers():
    result_levuriers = models.Levurier.objects.all()
    return render_template('levuriers.html', levuriers=result_levuriers)


@application.route('/login/', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('login.html', form=form)


def load_user(user_id):
    return models.User.objects.get(user_id)


if __name__ == '__main__':
    connect_to_mongodb()
    login_manager = prepare_login_manager(application)
    login_manager.user_loader(load_user)
    application.run(debug=False, host='0.0.0.0')
