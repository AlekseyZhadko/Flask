from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_books.db'
db = SQLAlchemy(app)


# Задание No2
# 📌 Создать базу данных для хранения информации о книгах в библиотеке.
# 📌 База данных должна содержать две таблицы: "Книги" и "Авторы".
# 📌 В таблице "Книги" должны быть следующие поля: id, название, год издания, количество экземпляров и id автора.
# 📌 В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# 📌 Необходимо создать связь между таблицами "Книги" и "Авторы".
# 📌 Написать функцию-обработчик, которая будет выводить список всех книг с указанием их авторов.
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    authors = db.relationship('Author', secondary='book_author', backref='books', lazy=True)

    def __repr__(self):
        return f'{self.name} {self.year} {self.count}'


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'{self.firstname} {self.lastname}'


class BookAuthor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_book = db.Column(db.Integer, db.ForeignKey('book.id'))
    id_autor = db.Column(db.Integer, db.ForeignKey('author.id'))
