from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Float)
    is_in_stock = db.Column(db.Boolean)

    def __init__(self, name, image=None, price=0.0, is_in_stock=True):
        self.name = name
        self.image = image
        self.price = price
        self.is_in_stock = is_in_stock

    def __repr__(self):
        return f'<Plant {self.name} | In Stock: {self.is_in_stock}>'

    def to_dict(self):
        """Convert the Plant instance to a dictionary for serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'price': self.price,
            'is_in_stock': self.is_in_stock
        }

    
