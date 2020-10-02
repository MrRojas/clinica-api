from config.db import db
import datetime

class PatientModel(db.Model):
    __tablename__ = 'patient'

    id = db.Column(db.Integer, db.Sequence('seq_patient_id', start=1, increment=1) , primary_key=True)
    name = db.Column(db.String(255))
    direccion = db.Column(db.String(255))
    birthday = db.Column(db.DateTime)
  
    status = db.Column(db.String(1) , default=1)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel')
 
    def __init__(self, name , direccion , birthday , user_id):
        self.nombre = nombre
        self.direccion = direccion
        self.birthday = birthday
        self.user_id = user_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()