from config.db import *
import datetime

class RolModel(db.Model):
    
    __tablename__ = 'roles'

    id = db.Column(db.Integer, db.Sequence('seq_roles_id', start=1, increment=1) , primary_key=True)
    name = db.Column(db.String(80))
    status = db.Column(db.String(1) , default=1)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    

    def __init__(self, name ):
        self.name = name

    def json(self):
        return {'name': self.name, 'price': self.price, 'store_id': self.store_id}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()  # simple TOP 1 select

    def save_to_db(self):  # Upserting data
        db.session.add(self)
        db.session.commit()  # Balla

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
