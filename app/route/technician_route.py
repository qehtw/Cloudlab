from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from flasgger import swag_from
from ..controllers.technician_controller import TechniciansController

technician_bp = Blueprint('technician', __name__, url_prefix='/technician')

@technician_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Technicians'],
    'responses': {
        200: {
            'description': 'List of all technicians',
            'examples': {
                'application/json': [
                    {'technician_id': 1, 'name': 'John Doe', 'email': 'john@example.com'}
                ]
            }
        }
    }
})
def get_all_technicians():
    technicians = TechniciansController.get_all_technicians()
    return make_response(jsonify(technicians), HTTPStatus.OK)

@technician_bp.route('/<int:technician_id>', methods=['GET'])
@swag_from({
    'tags': ['Technicians'],
    'parameters': [
        {'name': 'technician_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the technician'}
    ],
    'responses': {
        200: {'description': 'Technician found', 'examples': {'application/json': {'technician_id': 1, 'name': 'John Doe'}}},
        404: {'description': 'Technician not found'}
    }
})
def get_technician(technician_id):
    technician = TechniciansController.get_technician_by_id(technician_id)
    if technician:
        return make_response(jsonify(technician), HTTPStatus.OK)
    return make_response("Technician not found", HTTPStatus.NOT_FOUND)

@technician_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Technicians'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'email': {'type': 'string'}
                },
                'required': ['name', 'email']
            }
        }
    ],
    'responses': {
        201: {'description': 'Technician created'},
        400: {'description': 'Invalid input'}
    }
})
def create_technician():
    content = request.get_json()
    technician = TechniciansController.create_technician(content)
    return make_response(jsonify(technician), HTTPStatus.CREATED)

@technician_bp.route('/<int:technician_id>', methods=['PUT'])
@swag_from({
    'tags': ['Technicians'],
    'parameters': [
        {'name': 'technician_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the technician'},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'email': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Technician updated'},
        404: {'description': 'Technician not found'}
    }
})
def update_technician(technician_id: int):
    content = request.get_json()
    updated_technician = TechniciansController.update_technician(technician_id, content)
    if updated_technician:
        return make_response(jsonify(updated_technician), HTTPStatus.OK)
    return make_response("Technician not found", HTTPStatus.NOT_FOUND)

@technician_bp.route('/<int:technician_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Technicians'],
    'parameters': [
        {'name': 'technician_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the technician'}
    ],
    'responses': {
        200: {'description': 'Technician deleted'},
        404: {'description': 'Technician not found'}
    }
})
def delete_technician(technician_id: int):
    result = TechniciansController.delete_technician(technician_id)
    if result:
        return make_response("Technician deleted", HTTPStatus.OK)
    return make_response("Technician not found", HTTPStatus.NOT_FOUND)
