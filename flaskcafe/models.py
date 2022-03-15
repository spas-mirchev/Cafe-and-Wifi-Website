from flaskcafe import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Cafe(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250)) 
    map_url = db.Column(db.String(500), unique=True)
    img_url = db.Column(db.String(500), unique=True)
    location = db.Column(db.String(250))
    has_sockets = db.Column(db.Boolean, unique=False, default=True)
    has_toilet = db.Column(db.Boolean, unique=False, default=True)
    has_wifi = db.Column(db.Boolean, unique=False, default=True)
    can_take_calls = db.Column(db.Boolean, unique=False, default=True)
    seats = db.Column(db.String(500))
    coffee_price = db.Column(db.String(500))
    
    
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), unique=True, nullable=False)    