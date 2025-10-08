from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response, Response
from flasgger import swag_from
from ..controllers import UsersController
from ..models.user import insert_User, User

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['User'],
    'responses': {
        200: {
            'description': 'List of all users',
            'examples': {
                'application/json': [
                    {'user_id': 1, 'name': 'John', 'phone_number': '123', 'email': 'john@example.com', 'address': 'Address 1'}
                ]
            }
        }
    }
})
def get_all_users():
    users = UsersController.get_all_users()
    return make_response(jsonify(users), HTTPStatus.OK)

@user_bp.route('/<int:user_id>', methods=['GET'])
@swag_from({
    'tags': ['User'],
    'parameters': [
        {'name': 'user_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the user'}
    ],
    'responses': {
        200: {'description': 'User found'},
        404: {'description': 'User not found'}
    }
})
def get_user_route(user_id):
    user = UsersController.get_user(user_id)
    if user:
        return make_response(jsonify(user), HTTPStatus.OK)
    return make_response("User not found", HTTPStatus.NOT_FOUND)

@user_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['User'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'phone_number': {'type': 'string'},
                    'email': {'type': 'string'},
                    'address': {'type': 'string'}
                },
                'required': ['name', 'phone_number', 'email', 'address']
            }
        }
    ],
    'responses': {
        201: {'description': 'User created'},
        400: {'description': 'Invalid input'}
    }
})
def create_user():
    content = request.get_json()
    user = UsersController.create_user(content)
    return make_response(jsonify(user), HTTPStatus.CREATED)

@user_bp.route('/parametrized', methods=['POST'])
@swag_from({
    'tags': ['User'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'user_id': {'type': 'integer'},
                    'name': {'type': 'string'},
                    'phone_number': {'type': 'string'},
                    'email': {'type': 'string'},
                    'address': {'type': 'string'}
                },
                'required': ['user_id', 'name', 'phone_number', 'email', 'address']
            }
        }
    ],
    'responses': {
        201: {'description': 'Parametrized user inserted'}
    }
})
def insert_parametrized() -> Response:
    content = request.get_json()
    new_User = insert_User(
        user_id=content['user_id'],
        name=content['name'],
        phone_number=content['phone_number'],
        email=content['email'],
        address=content['address'],
    )
    return make_response(jsonify(new_User.put_into_dto()), HTTPStatus.CREATED)

@user_bp.route('/<int:user_id>', methods=['PUT'])
@swag_from({
    'tags': ['User'],
    'parameters': [
        {'name': 'user_id', 'in': 'path', 'type': 'integer', 'required': True},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'phone_number': {'type': 'string'},
                    'email': {'type': 'string'},
                    'address': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'User updated'},
        404: {'description': 'User not found'}
    }
})
def update_user(user_id: int):
    content = request.get_json()
    updated_user = UsersController.update_user(user_id, content)
    if updated_user:
        return make_response(jsonify(updated_user), HTTPStatus.OK)
    return make_response("User not found", HTTPStatus.NOT_FOUND)

@user_bp.route('/<int:user_id>', methods=['DELETE'])
@swag_from({
    'tags': ['User'],
    'parameters': [
        {'name': 'user_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {'description': 'User deleted'}
    }
})
def delete_user(user_id: int):
    UsersController.delete_user(user_id)
    return make_response("User deleted", HTTPStatus.OK)
