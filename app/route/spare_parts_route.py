from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from flasgger import swag_from
from ..controllers import spare_part_controller

spare_part_bp = Blueprint('spare_part', __name__, url_prefix='/spare_part')

@spare_part_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Spare Part'],
    'responses': {
        200: {
            'description': 'List of all spare parts',
            'examples': {
                'application/json': [
                    {'part_id': 1, 'name': 'Battery'},
                    {'part_id': 2, 'name': 'Screen'}
                ]
            }
        }
    }
})
def get_all_spare_parts():
    spare_parts = spare_part_controller.get_all_spare_parts()
    return make_response(jsonify(spare_parts), HTTPStatus.OK)

@spare_part_bp.route('/<int:part_id>', methods=['GET'])
@swag_from({
    'tags': ['Spare Part'],
    'parameters': [
        {'name': 'part_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the spare part'}
    ],
    'responses': {
        200: {'description': 'Spare Part found', 'examples': {'application/json': {'part_id': 1, 'name': 'Battery'}}},
        404: {'description': 'Spare Part not found'}
    }
})
def get_spare_part(part_id):
    spare_part = spare_part_controller.get_spare_part_by_id(part_id)
    if spare_part:
        return make_response(jsonify(spare_part), HTTPStatus.OK)
    return make_response("Spare Part not found", HTTPStatus.NOT_FOUND)

@spare_part_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Spare Part'],
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
        201: {'description': 'Spare Part created', 'examples': {'application/json': {'part_id': 3, 'name': 'Camera'}}}
    }
})
def create_spare_part():
    content = request.get_json()
    spare_part = spare_part_controller.create_spare_part(content)
    return make_response(jsonify(spare_part), HTTPStatus.CREATED)

@spare_part_bp.route('/<int:part_id>', methods=['PUT'])
@swag_from({
    'tags': ['Spare Part'],
    'parameters': [
        {'name': 'part_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the spare part'},
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
        200: {'description': 'Spare Part updated'},
        404: {'description': 'Spare Part not found'}
    }
})
def update_spare_part(part_id: int):
    content = request.get_json()
    updated_spare_part = spare_part_controller.update_spare_part(part_id, content)
    if updated_spare_part:
        return make_response(jsonify(updated_spare_part), HTTPStatus.OK)
    return make_response("Spare Part not found", HTTPStatus.NOT_FOUND)

@spare_part_bp.route('/<int:part_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Spare Part'],
    'parameters': [
        {'name': 'part_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the spare part'}
    ],
    'responses': {
        200: {'description': 'Spare Part deleted'},
        404: {'description': 'Spare Part not found'}
    }
})
def delete_spare_part(part_id: int):
    result = spare_part_controller.delete_spare_part(part_id)
    if result:
        return make_response("Spare Part deleted", HTTPStatus.OK)
    return make_response("Spare Part not found", HTTPStatus.NOT_FOUND)

@spare_part_bp.route('/aggregated_quantities', methods=['GET'])
@swag_from({
    'tags': ['Spare Part'],
    'responses': {
        200: {
            'description': 'Aggregated quantities of spare parts',
            'examples': {'application/json': {'Battery': 10, 'Screen': 5}}
        }
    }
})
def get_aggregated_quantities():
    aggregated_quantities = spare_part_controller.get_aggregated_quantities()
    return jsonify(aggregated_quantities)
