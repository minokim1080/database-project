from today import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    gender = db.Column(db.String(), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    bmi = db.Column(db.Float, nullable=False)

class Cloth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    classification = db.Column(db.String(), nullable=False)
    cloth_type = db.Column(db.String(), nullable=False)
    fit = db.Column(db.String(), nullable=False)
    color = db.Column(db.String(), nullable=False)

