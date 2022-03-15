from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, URL, ValidationError
from flaskcafe.models import Users, Cafe

my_choices = ['0-10', '10-20', '20-30', '30-40', '50+'] 
class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired(), Length(min=2, max=50)])
    map_url = StringField('Cafe location on Google Maps(URL)', validators=[DataRequired(), URL()])
    img_url = StringField('Image (URL)', validators=[DataRequired(), URL()])
    location = StringField('Location', validators=[DataRequired()])
    has_sockets = BooleanField('Has sockets', default=False)
    has_toilet = BooleanField('Has toilet (Yes or not)', default=False)
    has_wifi = BooleanField('Has wifi (Yes or not)', default=False)
    can_take_calls = BooleanField('Can take calls (Yes or not)', default=False)
    seats = SelectField('How many seats',choices = my_choices, validators=[DataRequired()])
    coffee_price = StringField('Coffee price', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
    def validate_name(self, name):
        user = Cafe.query.filter_by(name=name.data).first()
        if user:
           raise ValidationError('That name is already exist.', 'error')
    
               
    
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])   
    submit = SubmitField('Sign Up') 
    
    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')
    
   
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired('Oppa'), Email()])
    password = PasswordField('Password', validators=[DataRequired('Oppala')]) 
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')