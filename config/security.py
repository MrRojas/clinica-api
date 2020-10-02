from werkzeug.security import safe_str_cmp

from app.models.user import UserModel


def authenticate(identification, password):
    user = UserModel.find_by_identification(identification)
    if user and safe_str_cmp(user.password, password) and user['status'] == '1':
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
