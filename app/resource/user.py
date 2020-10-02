from flask_restful import Resource, reqparse
from app.models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
    parser.add_argument('identification', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('email', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('phone', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('rol_id', type=str, required=True, help='This field cannot be left blank')

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['identification']):
            return {'message': 'UserModel has already been created, aborting.'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message': 'user has been created successfully.'}, 201
