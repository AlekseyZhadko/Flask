import random

from flask import Flask, render_template

from Task_1.models import db, Student, Faculty, Estimate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-student")
def add_data():
    for i in range(4):
        faculty = Faculty(
            name=f'faculty_{i}'
        )
        db.session.add(faculty)

    for i in range(10):
        student = Student(
            firstname=f'firstname_{i}',
            lastname=f'lastname_{i}',
            age=random.randint(18, 100),
            gender=random.choice(['man', 'woman']),
            group=random.randint(1, 10),
            id_faculty=random.randint(1, 3)
        )
        db.session.add(student)

    db.session.commit()
    print('data add for db, good!')


@app.get('/')
def get_student():
    students = Student.query.all()
    context = {
        'students': students
    }
    return render_template('students.html', **context)
