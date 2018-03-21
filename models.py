from app import db


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    contact_name = db.Column(db.String(200))
    contact_phone = db.Column(db.String(100))
    contact_email = db.Column(db.String(150))
    status = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    confirmed = db.Column(db.DateTime)
    comment = db.Column(db.Text)
    price = db.Column(db.Float)
