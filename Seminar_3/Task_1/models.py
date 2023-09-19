from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)


# Задание No1
# 📌 Создать базу данных для хранения информации о студентах университета.
# 📌 База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# 📌 В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
# 📌 В таблице "Факультеты" должны быть следующие поля: id и название факультета.
# 📌 Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# 📌 Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их факультета.

# Задание No3
# 📌 Доработаем задача про студентов
# 📌 Создать базу данных для хранения информации о студентах и их оценках в учебном заведении.
# 📌 База данных должна содержать две таблицы: "Студенты" и "Оценки".
# 📌 В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
# 📌 В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.
# 📌 Необходимо создать связь между таблицами "Студенты" и "Оценки".
# 📌 Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их оценок.
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(80), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    id_faculty = db.Column(db.Integer, db.ForeignKey('faculty.id'))

    def __repr__(self):
        return f'Student: {self.firstname} {self.lastname}'


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    students = db.relationship('Student', backref='faculty', lazy=True)

    def __repr__(self):
        return f'Faculty: {self.name}'
