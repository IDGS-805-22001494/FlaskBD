from urllib3 import request
from flask import Flask, render_template, flash, g, request # type: ignore
from flask import flash # type: ignore
from flask_wtf.csrf import CSRFProtect # type: ignore
from flask import g # type: ignore
from config import DevelopmentConfig

import forms
from models import Alumnos
from models import db


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route("/")
@app.route("/index")
def index():
    create_form = forms.UserForm2(request.form)
    alumno=Alumnos.query.all()
    
    return render_template("index.html", form=create_form, alumno=alumno)

@app.route("/detalles")
def detalles():
    create_form = forms.UserForm2(request.form)
    if request.method == 'GET':
        id=request.args.get('id')
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        nom=alum1.nombre
        ape=alum1.apaterno
        email=alum1.email
    return render_template("detalles.html", form=create_form, nombre=nom, apaterno=ape, email=email)
    
    
@app.route('/Alumnos1', method=['GET', 'POST'])
def Alumnos1():
    create_form=forms.UserForm2(request.form)
    if request.method=='POST':
        alum=Alumnos(nombre=create_form.nombre.data, apaterno=create_form.apaterno.data, email=create_form.email.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("Alumnos1.html", form=create_form)
if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
       