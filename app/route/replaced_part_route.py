from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from flasgger import swag_from
from ..controllers import replaced_part_controller

replaced_part_bp = Blueprint('replaced_part', __name__, url_prefix='/replaced_part')

@replaced_part_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Replaced Part'],
    'responses': {
        200: {
            'description': 'List of all replaced parts',
            'examples': {
                'application/json': [
                    {'replaced_part_id': 1, 'name': 'Screen'},
                    {'replaced_part_id': 2, 'name': 'Battery'}
                ]
            }
        }
    }
})
def get_all_replaced_parts():
    replaced_parts = replaced_part_controller.get_all_replaced_parts()
    return make_response(jsonify(replaced_parts), HTTPStatus.OK)

@replaced_part_bp.route('/<int:replaced_part_id>', methods=['GET'])
@swag_from({
    'tags': ['Replaced Part'],
    'parameters': [
        {'name': 'replaced_part_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the replaced part'}
    ],
    'responses': {
        200: {'description': 'Replaced Part found', 'examples': {'application/json': {'replaced_part_id': 1, 'name': 'Screen'}}},
        404: {'description': 'Replaced Part not found'}
    }
})
def get_replaced_part(replaced_part_id):
    replaced_part = replaced_part_controller.get_replaced_part_by_id(replaced_part_id)
    if replaced_part:
        return make_response(jsonify(replaced_part), HTTPStatus.OK)
    return make_response("Replaced Part not found", HTTPStatus.NOT_FOUND)

@replaced_part_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Replaced Part'],
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
        201: {'description': 'Replaced Part created', 'examples': {'application/json': {'replaced_part_id': 3, 'name': 'Camera'}}}
    }
})
def create_replaced_part():
    content = request.get_json()
    replaced_part = replaced_part_controller.create_replaced_part(content)
    return make_response(jsonify(replaced_part), HTTPStatus.CREATED)

@replaced_part_bp.route('/<int:replaced_part_id>', methods=['PUT'])
@swag_from({
    'tags': ['Replaced Part'],
    'parameters': [
        {'name': 'replaced_part_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the replaced part'},
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
        200: {'description': 'Replaced Part updated'},
        404: {'description': 'Replaced Part not found'}
    }
})
def update_replaced_part(replaced_part_id: int):
    content = request.get_json()
    updated_replaced_part = replaced_part_controller.update_replaced_part(replaced_part_id, content)
    if updated_replaced_part:
        return make_response(jsonify(updated_replaced_part), HTTPStatus.OK)
    return make_response("Replaced Part not found", HTTPStatus.NOT_FOUND)

@replaced_part_bp.route('/<int:replaced_part_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Replaced Part'],
    'parameters': [
        {'name': 'replaced_part_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the replaced part'}
    ],
    'responses': {
        200: {'description': 'Replaced Part deleted'},
        404: {'description': 'Replaced Part not found'}
    }
})
def delete_replaced_part(replaced_part_id: int):
    result = replaced_part_controller.delete_replaced_part(replaced_part_id)
    if result:
        return make_response("Replaced Part deleted", HTTPStatus.OK)
    return make_response("Replaced Part not found", HTTPStatus.NOT_FOUND)
