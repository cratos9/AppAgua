from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config.from_mapping(
        DEGUB = True,
        SECRET_KEY = 'llave ultra secreta que nadie sabe',
        SQLALCHEMY_DATABASE_URI = "sqlite:///agua.db"
    )
    db.init_app(app)
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    with app.app_context():
        db.create_all()
    
    return app