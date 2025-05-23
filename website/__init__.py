from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "notes.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
    db.init_app(app)



    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')  

    from .models import User, Note
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()    
    login_manager.login_view = 'auth.login'  # redirect to login page if not logged in
    login_manager.init_app(app)   
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))   # get user by id   

    return app