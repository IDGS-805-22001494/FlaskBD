from flask import Flask, render_template # type: ignore
from flask import flash # type: ignore
from flask_wtf.csrf import CSRFProtect # type: ignore
from flask import g # type: ignore
from config import DevelopmentConfig

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
	return render_template("index.html")



if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
       