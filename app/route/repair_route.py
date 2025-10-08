from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from flasgger import swag_from
from ..controllers import repair_controller

repair_bp = Blueprint('repair', __name__, url_prefix='/repair')

@repair_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Repair'],
    'responses': {
        200: {
            'description': 'List of all repairs',
            'examples': {
                'application/json': [
                    {'repair_id': 1, 'description': 'Fix screen', 'cost': 100},
                    {'repair_id': 2, 'description': 'Replace battery', 'cost': 50}
                ]
            }
        }
    }
})
def get_all_repairs():
    repairs = repair_controller.get_all_repairs()
    return make_response(jsonify(repairs), HTTPStatus.OK)

@repair_bp.route('/<int:repair_id>', methods=['GET'])
@swag_from({
    'tags': ['Repair'],
    'parameters': [
        {'name': 'repair_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the repair'}
    ],
    'responses': {
        200: {'description': 'Repair found', 'examples': {'application/json': {'repair_id': 1, 'description': 'Fix screen', 'cost': 100}}},
        404: {'description': 'Repair not found'}
    }
})
def get_repair(repair_id):
    repair = repair_controller.get_repair_by_id(repair_id)
    if repair:
        return make_response(jsonify(repair), HTTPStatus.OK)
    return make_response("Repair not found", HTTPStatus.NOT_FOUND)

@repair_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Repair'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'description': {'type': 'string'},
                    'cost': {'type': 'number'}
                },
                'required': ['description', 'cost']
            }
        }
    ],
    'responses': {
        201: {'description': 'Repair created', 'examples': {'application/json': {'repair_id': 3, 'description': 'Replace screen', 'cost': 120}}}
    }
})
def create_repair():
    content = request.get_json()
    repair = repair_controller.create_repair(content)
    return make_response(jsonify(repair), HTTPStatus.CREATED)

@repair_bp.route('/<int:repair_id>', methods=['PUT'])
@swag_from({
    'tags': ['Repair'],
    'parameters': [
        {'name': 'repair_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the repair'},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'description': {'type': 'string'},
                    'cost': {'type': 'number'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Repair updated'},
        404: {'description': 'Repair not found'}
    }
})
def update_repair(repair_id: int):
    content = request.get_json()
    updated_repair = repair_controller.update_repair(repair_id, content)
    if updated_repair:
        return make_response(jsonify(updated_repair), HTTPStatus.OK)
    return make_response("Repair not found", HTTPStatus.NOT_FOUND)

@repair_bp.route('/<int:repair_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Repair'],
    'parameters': [
        {'name': 'repair_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the repair'}
    ],
    'responses': {
        200: {'description': 'Repair deleted'},
        404: {'description': 'Repair not found'}
    }
})
def delete_repair(repair_id: int):
    result = repair_controller.delete_repair(repair_id)
    if result:
        return make_response("Repair deleted", HTTPStatus.OK)
    return make_response("Repair not found", HTTPStatus.NOT_FOUND)
