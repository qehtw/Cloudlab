from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from flasgger import swag_from
from ..controllers import repair_type_controller

repair_type_bp = Blueprint('repair_type', __name__, url_prefix='/repair_type')

@repair_type_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Repair Type'],
    'responses': {
        200: {
            'description': 'List of all repair types',
            'examples': {
                'application/json': [
                    {'repair_type_id': 1, 'name': 'Screen Repair'},
                    {'repair_type_id': 2, 'name': 'Battery Replacement'}
                ]
            }
        }
    }
})
def get_all_repair_types():
    repair_types = repair_type_controller.get_all_repair_types()
    return make_response(jsonify(repair_types), HTTPStatus.OK)

@repair_type_bp.route('/<int:repair_type_id>', methods=['GET'])
@swag_from({
    'tags': ['Repair Type'],
    'parameters': [
        {'name': 'repair_type_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the repair type'}
    ],
    'responses': {
        200: {'description': 'Repair Type found', 'examples': {'application/json': {'repair_type_id': 1, 'name': 'Screen Repair'}}},
        404: {'description': 'Repair Type not found'}
    }
})
def get_repair_type(repair_type_id):
    repair_type = repair_type_controller.get_repair_type_by_id(repair_type_id)
    if repair_type:
        return make_response(jsonify(repair_type), HTTPStatus.OK)
    return make_response("Repair Type not found", HTTPStatus.NOT_FOUND)

@repair_type_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Repair Type'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'}
                },
                'required': ['name']
            }
        }
    ],
    'responses': {
        201: {'description': 'Repair Type created', 'examples': {'application/json': {'repair_type_id': 3, 'name': 'Camera Repair'}}}
    }
})
def create_repair_type():
    content = request.get_json()
    repair_type = repair_type_controller.create_repair_type(content)
    return make_response(jsonify(repair_type), HTTPStatus.CREATED)

@repair_type_bp.route('/<int:repair_type_id>', methods=['PUT'])
@swag_from({
    'tags': ['Repair Type'],
    'parameters': [
        {'name': 'repair_type_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the repair type'},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Repair Type updated'},
        404: {'description': 'Repair Type not found'}
    }
})
def update_repair_type(repair_type_id: int):
    content = request.get_json()
    updated_repair_type = repair_type_controller.update_repair_type(repair_type_id, content)
    if updated_repair_type:
        return make_response(jsonify(updated_repair_type), HTTPStatus.OK)
    return make_response("Repair Type not found", HTTPStatus.NOT_FOUND)

@repair_type_bp.route('/<int:repair_type_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Repair Type'],
    'parameters': [
        {'name': 'repair_type_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the repair type'}
    ],
    'responses': {
        200: {'description': 'Repair Type deleted'},
        404: {'description': 'Repair Type not found'}
    }
})
def delete_repair_type(repair_type_id: int):
    result = repair_type_controller.delete_repair_type(repair_type_id)
    if result:
        return make_response("Repair Type deleted", HTTPStatus.OK)
    return make_response("Repair Type not found", HTTPStatus.NOT_FOUND)
