from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.auth.models import User

def email_exists(form, field):
    email=User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError('Email already Exists!!!!')

class RegistrationForm(FlaskForm):
    name=StringField('Name', validators=[DataRequired(), Length(4,16, message='Between 4 to 16 characters')])
    email=StringField('E-mail', validators=[DataRequired(), Email(), email_exists])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Password must match !!!!')])
    #password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message=' Password must match')])
    confirm=PasswordField('Confirm', validators=[DataRequired()])
    submit=SubmitField('Register')

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(), Email()])
    password=PasswordField('Password', validators=[DataRequired()])
    stay_loggedin=BooleanField('Remember Me')
    submit=SubmitField('Login')
    
    
    
"""
sugerencia de copitlot

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.auth.models import User

# Validador personalizado para verificar si el email ya existe en la base de datos
def email_exists(form, field):
    email = User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError('El email ya está registrado.')

class RegistrationForm(FlaskForm):
    name = StringField('Nombre', validators=[
        DataRequired(message="El nombre es obligatorio."),
        Length(4, 16, message="El nombre debe tener entre 4 y 16 caracteres.")
    ])
    
    email = StringField('Correo electrónico', validators=[
        DataRequired(message="El email es obligatorio."),
        Email(message="Introduce un correo válido."),
        email_exists
    ])
    
    password = PasswordField('Contraseña', validators=[
        DataRequired(message="La contraseña es obligatoria."),
        Length(6, 20, message="La contraseña debe tener entre 6 y 20 caracteres.")
    ])
    
    confirm = PasswordField('Confirmar contraseña', validators=[
        DataRequired(message="Debe confirmar su contraseña."),
        EqualTo('password', message="Las contraseñas deben coincidir.")
    ])
    
    submit = SubmitField('Registrarse')

class LoginForm(FlaskForm):
    email = StringField('Correo electrónico', validators=[
        DataRequired(message="El email es obligatorio."),
        Email(message="Introduce un correo válido.")
    ])
    
    password = PasswordField('Contraseña', validators=[
        DataRequired(message="La contraseña es obligatoria.")
    ])
    
    stay_loggedin = BooleanField('Recordarme')
    
    submit = SubmitField('Iniciar sesión')
"""    