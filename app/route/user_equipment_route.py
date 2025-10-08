from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from flasgger import swag_from
from ..controllers.user_equipment_controller import UserEquipmentController

user_equipment_bp = Blueprint('user_equipment', __name__, url_prefix='/user_equipment')

@user_equipment_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['User Equipment'],
    'responses': {
        200: {
            'description': 'List of all user equipment',
            'examples': {
                'application/json': [
                    {'user_equipment_id': 1, 'user_id': 1, 'equipment_id': 2}
                ]
            }
        }
    }
})
def get_all_user_equipment():
    user_equipment = UserEquipmentController.get_all_user_equipment()
    return make_response(jsonify(user_equipment), HTTPStatus.OK)

@user_equipment_bp.route('/<int:user_equipment_id>', methods=['GET'])
@swag_from({
    'tags': ['User Equipment'],
    'parameters': [
        {'name': 'user_equipment_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the user equipment'}
    ],
    'responses': {
        200: {'description': 'User equipment found', 'examples': {'application/json': {'user_equipment_id': 1, 'user_id': 1, 'equipment_id': 2}}},
        404: {'description': 'User equipment not found'}
    }
})
def get_user_equipment(user_equipment_id: int):
    user_equipment = UserEquipmentController.get_user_equipment_by_id(user_equipment_id)
    if user_equipment:
        return make_response(jsonify(user_equipment), HTTPStatus.OK)
    return make_response("User equipment not found", HTTPStatus.NOT_FOUND)

@user_equipment_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['User Equipment'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'user_id': {'type': 'integer'},
                    'equipment_id': {'type': 'integer'}
                },
                'required': ['user_id', 'equipment_id']
            }
        }
    ],
    'responses': {
        201: {'description': 'User equipment created'},
        400: {'description': 'Invalid input'}
    }
})
def create_user_equipment():
    content = request.get_json()
    user_equipment = UserEquipmentController.create_user_equipment(content)
    return make_response(jsonify(user_equipment), HTTPStatus.CREATED)

@user_equipment_bp.route('/<int:user_equipment_id>', methods=['PUT'])
@swag_from({
    'tags': ['User Equipment'],
    'parameters': [
        {'name': 'user_equipment_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the user equipment'},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'user_id': {'type': 'integer'},
                    'equipment_id': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'User equipment updated'},
        404: {'description': 'User equipment not found'}
    }
})
def update_user_equipment(user_equipment_id: int):
    content = request.get_json()
    updated_user_equipment = UserEquipmentController.update_user_equipment(user_equipment_id, content)
    if updated_user_equipment:
        return make_response(jsonify(updated_user_equipment), HTTPStatus.OK)
    return make_response("User equipment not found", HTTPStatus.NOT_FOUND)

@user_equipment_bp.route('/<int:user_equipment_id>', methods=['DELETE'])
@swag_from({
    'tags': ['User Equipment'],
    'parameters': [
        {'name': 'user_equipment_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the user equipment'}
    ],
    'responses': {
        200: {'description': 'User equipment deleted'},
        404: {'description': 'User equipment not found'}
    }
})
def delete_user_equipment(user_equipment_id: int):
    result = UserEquipmentController.delete_user_equipment(user_equipment_id)
    if result:
        return make_response("User equipment deleted", HTTPStatus.OK)
    return make_response("User equipment not found", HTTPStatus.NOT_FOUND)
