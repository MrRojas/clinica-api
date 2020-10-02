from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import psycopg2

from config.env import databaseConfig
from app.resource.user import UserRegister
from config.security import authenticate, identity
from config.db import *
from app.models.rol import RolModel 
from app.models.user import UserModel 
from app.models.hospital import HospitalModel 
from app.models.patient import PatientModel 

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = databaseConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Dese.Decent.Pups.BOOYO0OST'
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail()


@app.before_first_request
def create_tables():
    db.create_all()

# auth endpoint
jwt = JWT(app, authenticate, identity) 
# endpoint app 
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from config.db import db  #Avoid circular import
    db.init_app(app)
    # debug=False for produccion 
    mail.init_app(app)
    app.run(debug=True) 

    


