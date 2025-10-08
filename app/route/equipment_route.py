from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from flasgger import swag_from
from ..controllers import equipment_controller

equipment_bp = Blueprint('equipment', __name__, url_prefix='/equipment')

@equipment_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Equipment'],
    'responses': {
        200: {
            'description': 'List of all equipment',
            'examples': {
                'application/json': [
                    {'equipment_id': 1, 'name': 'Drill', 'status': 'available'},
                    {'equipment_id': 2, 'name': 'Hammer', 'status': 'in use'}
                ]
            }
        }
    }
})
def get_all_equipment():
    equipment = equipment_controller.get_all_equipment()
    return make_response(jsonify(equipment), HTTPStatus.OK)

@equipment_bp.route('/<int:equipment_id>', methods=['GET'])
@swag_from({
    'tags': ['Equipment'],
    'parameters': [
        {'name': 'equipment_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the equipment'}
    ],
    'responses': {
        200: {
            'description': 'Equipment found',
            'examples': {'application/json': {'equipment_id': 1, 'name': 'Drill', 'status': 'available'}}
        },
        404: {'description': 'Equipment not found'}
    }
})
def get_equipment(equipment_id: int):
    equipment = equipment_controller.get_equipment(equipment_id)
    if equipment:
        return make_response(jsonify(equipment), HTTPStatus.OK)
    return make_response("Equipment not found", HTTPStatus.NOT_FOUND)

@equipment_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Equipment'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'status': {'type': 'string'}
                },
                'required': ['name', 'status']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Equipment created',
            'examples': {'application/json': {'equipment_id': 3, 'name': 'Saw', 'status': 'available'}}
        }
    }
})
def create_equipment():
    content = request.get_json()
    equipment = equipment_controller.create_equipment(content)
    return make_response(jsonify(equipment), HTTPStatus.CREATED)

@equipment_bp.route('/<int:equipment_id>', methods=['PUT'])
@swag_from({
    'tags': ['Equipment'],
    'parameters': [
        {'name': 'equipment_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the equipment'},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'status': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Equipment updated'},
        404: {'description': 'Equipment not found'}
    }
})
def update_equipment(equipment_id: int):
    content = request.get_json()
    updated_equipment = equipment_controller.update_equipment(equipment_id, content)
    if updated_equipment:
        return make_response(jsonify(updated_equipment), HTTPStatus.OK)
    return make_response("Equipment not found", HTTPStatus.NOT_FOUND)

@equipment_bp.route('/<int:equipment_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Equipment'],
    'parameters': [
        {'name': 'equipment_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the equipment'}
    ],
    'responses': {
        200: {'description': 'Equipment deleted'},
        404: {'description': 'Equipment not found'}
    }
})
def delete_equipment(equipment_id: int):
    result = equipment_controller.delete_equipment(equipment_id)
    if result:
        return make_response("Equipment deleted", HTTPStatus.OK)
    return make_response("Equipment not found", HTTPStatus.NOT_FOUND)
