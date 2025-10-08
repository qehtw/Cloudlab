from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from flasgger import swag_from
from ..controllers import technician_repairs_controller

technician_repairs_bp = Blueprint('technician_repairs', __name__, url_prefix='/technician_repairs')

@technician_repairs_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Technician Repairs'],
    'responses': {
        200: {
            'description': 'List of all technician repairs',
            'examples': {
                'application/json': [
                    {'technician_repair_id': 1, 'technician_id': 5, 'repair_id': 10}
                ]
            }
        }
    }
})
def get_all_technician_repairs():
    technician_repairs = technician_repairs_controller.get_all_technician_repairs()
    return make_response(jsonify(technician_repairs), HTTPStatus.OK)

@technician_repairs_bp.route('/<int:technician_repair_id>', methods=['GET'])
@swag_from({
    'tags': ['Technician Repairs'],
    'parameters': [
        {'name': 'technician_repair_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the technician repair'}
    ],
    'responses': {
        200: {'description': 'Technician Repair found', 'examples': {'application/json': {'technician_repair_id': 1, 'technician_id': 5, 'repair_id': 10}}},
        404: {'description': 'Technician Repair not found'}
    }
})
def get_technician_repair(technician_repair_id):
    technician_repair = technician_repairs_controller.get_technician_repair_by_id(technician_repair_id)
    if technician_repair:
        return make_response(jsonify(technician_repair), HTTPStatus.OK)
    return make_response("Technician Repair not found", HTTPStatus.NOT_FOUND)

@technician_repairs_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Technician Repairs'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'technician_id': {'type': 'integer'},
                    'repair_id': {'type': 'integer'}
                },
                'required': ['technician_id', 'repair_id']
            }
        }
    ],
    'responses': {
        201: {'description': 'Technician Repair created'},
        400: {'description': 'Technician or Repair not found'}
    }
})
def create_technician_repair():
    content = request.get_json()
    technician_repair = technician_repairs_controller.create_technician_repair(content)
    if technician_repair:
        return make_response(jsonify(technician_repair), HTTPStatus.CREATED)
    return make_response({"error": "Technician or Repair not found"}, HTTPStatus.BAD_REQUEST)

@technician_repairs_bp.route('/<int:technician_repair_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Technician Repairs'],
    'parameters': [
        {'name': 'technician_repair_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the technician repair'}
    ],
    'responses': {
        200: {'description': 'Technician Repair deleted'},
        404: {'description': 'Technician Repair not found'}
    }
})
def delete_technician_repair(technician_repair_id: int):
    result = technician_repairs_controller.delete_technician_repair(technician_repair_id)
    if result:
        return make_response("Technician Repair deleted", HTTPStatus.OK)
    return make_response("Technician Repair not found", HTTPStatus.NOT_FOUND)
