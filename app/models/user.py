from config.db import db
import datetime

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, db.Sequence('seq_users_id', start=1, increment=1) , primary_key=True)
    identification = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    password = db.Column(db.String(255))
    status = db.Column(db.String(1) , default=2) # 2 = user new 
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    rol = db.relationship('RolModel')
 
    def __init__(self, identification, password, email, phone, rol_id):
        self.identification = identification
        self.password = password
        self.email = email
        self.phone = phone
        self.rol_id = rol_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def find_by_identification(cls, identification):
        return cls.query.filter_by(identification=identification).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()