from http import HTTPStatus
from ..controllers import UsersController
from flask import Blueprint, jsonify, Response, request, make_response, abort
from ..models.user import insert_User , User

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('', methods=['GET'])
def get_all_users():
    users = UsersController.get_all_users()
    return make_response(jsonify(users), HTTPStatus.OK)

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user_route(user_id):
    user = UsersController.get_user(user_id)  # Викликаємо метод get_user через клас
    if user:
        return make_response(jsonify(user), HTTPStatus.OK)
    return make_response("User not found", HTTPStatus.NOT_FOUND)

@user_bp.route('', methods=['POST'])
def create_user():
    content = request.get_json()
    user = UsersController.create_user(content)  # Викликаємо метод create_user через клас
    return make_response(jsonify(user), HTTPStatus.CREATED)

@user_bp.route('/parametrized', methods=['POST'])
def insert_parametrized() -> Response:
    content = request.get_json()
    new_User = insert_User(
        user_id = content['user_id'],
        name = content['name'],
        phone_number= content['phone_number'],
        email=content['email'],
        address= content['address'],
        )
    return make_response(jsonify(new_User.put_into_dto()), HTTPStatus.CREATED)

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id: int):
    content = request.get_json()
    updated_user = UsersController.update_user(user_id, content)  # Викликаємо метод update_user через клас
    if updated_user:
        return make_response(jsonify(updated_user), HTTPStatus.OK)
    return make_response("User not found", HTTPStatus.NOT_FOUND)

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    UsersController.delete_user(user_id)  # Викликаємо метод delete_user через клас
    return make_response("User deleted", HTTPStatus.OK)
