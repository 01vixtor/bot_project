from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    from models import User
    with app.app_context():
        db.create_all()

    from routes import main
    app.register_blueprint(main)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
