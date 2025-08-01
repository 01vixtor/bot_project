from app import db
from flask_login import UserMixin
from app import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class BotConfig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_text = db.Column(db.Text, nullable=False)
    interval_minutes = db.Column(db.Integer, default=60)
    valid_time_minutes = db.Column(db.Integer, default=10)
    random_min = db.Column(db.Float, default=1.0)
    random_max = db.Column(db.Float, default=2.0)
