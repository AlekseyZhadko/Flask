import base64

from flask import Flask, render_template, request, flash, redirect, url_for
from Task_4.models import db, User
from flask_wtf import CSRFProtect

from Seminar_3.Task_4.forms import RegisterForm

# генерация ключа
# import secrets
# secrets.token_hex()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_user.db'
db.init_app(app)
app.config['SECRET_KEY'] = '35f34e6a375053a029c051f2c9323e55c57053f59522e97c445afc5724a2b695'
csrf = CSRFProtect(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        birthday = form.birthday.data
        email = form.email.data
        password = form.password.data

        user_name = User.query.filter(User.username == username).all()
        user_email = User.query.filter(User.email == email).all()
        if len(user_name) + len(user_email) == 0:
            user = User(
                username=username,
                birthday=birthday,
                email=email,
                password=f'{base64.b64decode(password)}'
            )
            db.session.add(user)
            db.session.commit()
            flash('Регистрация успешно выполнена!', 'success')
            return redirect(url_for('register'))
        else:
            flash('Регистрация не выполнена: пользователь с таким именем существует!', 'danger')
            return redirect(url_for('register'))
    return render_template('register.html', form=form)
