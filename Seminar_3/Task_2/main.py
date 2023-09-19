import random

from flask import Flask, render_template

from Task_2.models import db, Book, Author, BookAuthor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_books.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-book")
def add_data():
    for i in range(10):
        book = Book(
            name=f'name_{i}',
            year=random.randint(1800, 2023),
            count=random.randint(1, 10)
        )
        db.session.add(book)

    for i in range(15):
        author = Author(
            firstname=f'firstname_{i}',
            lastname=f'lastname_{i}',
        )
        db.session.add(author)

    for i in range(10):
        book_author = BookAuthor(
            id_book=random.randint(1, 9),
            id_autor=random.randint(1, 14)
        )
        db.session.add(book_author)

    db.session.commit()

    print('data add for db, good!')


@app.get('/book/')
def get_book():
    books = Book.query.all()
    context = {
        'books': books
    }
    return render_template('register.html', **context)
