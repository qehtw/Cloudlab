from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from ..controllers import replaced_part_controller

replaced_part_bp = Blueprint('replaced_part', __name__, url_prefix='/replaced_part')

@replaced_part_bp.route('', methods=['GET'])
def get_all_replaced_parts():
    replaced_parts = replaced_part_controller.get_all_replaced_parts()
    return make_response(jsonify(replaced_parts), HTTPStatus.OK)

@replaced_part_bp.route('/<int:replaced_part_id>', methods=['GET'])
def get_replaced_part(replaced_part_id):
    replaced_part = replaced_part_controller.get_replaced_part_by_id(replaced_part_id)
    if replaced_part:
        return make_response(jsonify(replaced_part), HTTPStatus.OK)
    return make_response("Replaced Part not found", HTTPStatus.NOT_FOUND)

@replaced_part_bp.route('', methods=['POST'])
def create_replaced_part():
    content = request.get_json()
    replaced_part = replaced_part_controller.create_replaced_part(content)
    return make_response(jsonify(replaced_part), HTTPStatus.CREATED)

@replaced_part_bp.route('/<int:replaced_part_id>', methods=['PUT'])
def update_replaced_part(replaced_part_id: int):
    content = request.get_json()
    updated_replaced_part = replaced_part_controller.update_replaced_part(replaced_part_id, content)
    if updated_replaced_part:
        return make_response(jsonify(updated_replaced_part), HTTPStatus.OK)
    return make_response("Replaced Part not found", HTTPStatus.NOT_FOUND)

@replaced_part_bp.route('/<int:replaced_part_id>', methods=['DELETE'])
def delete_replaced_part(replaced_part_id: int):
    result = replaced_part_controller.delete_replaced_part(replaced_part_id)
    if result:
        return make_response("Replaced Part deleted", HTTPStatus.OK)
    return make_response("Replaced Part not found", HTTPStatus.NOT_FOUND)
