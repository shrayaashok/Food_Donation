from .. import db

class Food(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    location = db.Column(db.String(200))
    expiry_time = db.Column(db.String(50))
    donor_id = db.Column(db.Integer)
    status = db.Column(db.String(20), default="available")