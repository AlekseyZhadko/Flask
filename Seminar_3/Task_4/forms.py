from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, PasswordField, DateField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp


class RegisterForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    birthday = DateField('Date', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    check = BooleanField('согласие на обработку персональных данных', default=False, validators=[DataRequired()])
