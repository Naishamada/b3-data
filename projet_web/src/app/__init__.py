from flask import Flask, render_template, request, url_for, flash, redirect

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SECRET_KEY'] = 'hardsecretkey'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"

    id=db.Column(db.Integer, primary_key=True)
    rna_id=db.Column(db.String(40), nullable=True)
    rna_id_ex=db.Column(db.String(40), nullable=True)
    gestion=db.Column(db.String(40), nullable=True)

class CreateAssosForm(FlaskForm):
    rna_id = StringField('RNA ID', validators=[InputRequired()])
    rna_id_ex = StringField('RNA ID EX', validators=[InputRequired()])
    gestion = StringField('Gestion', validators=[InputRequired()])

@app.route('/')
def home():
    return render_template('home.html')

#create_assos route
@app.route('/create_assos' , methods = ['GET', 'POST'])

def create_assos():
    form = CreateAssosForm()
    if form.validate_on_submit():
        rna_id = form.rna_id.data
        rna_id_ex = form.rna_id_ex.data
        gestion = form.gestion.data
        new_assos = Data(rna_id=rna_id, rna_id_ex=rna_id_ex, gestion=gestion)
        db.session.add(new_assos) 
        db.session.commit() 
        flash("Assos créer avec succès")
    return render_template('create_assos.html', form=form)
 

@app.route('/assos')
def assos(datas=None):
    datas=Data.query.limit(10).all()
    return render_template('assos.html', datas=datas)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '-main-':
    app.run()