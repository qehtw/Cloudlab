from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from ..controllers import spare_part_controller

spare_part_bp = Blueprint('spare_part', __name__, url_prefix='/spare_part')

@spare_part_bp.route('', methods=['GET'])
def get_all_spare_parts():
    spare_parts = spare_part_controller.get_all_spare_parts()
    return make_response(jsonify(spare_parts), HTTPStatus.OK)

@spare_part_bp.route('/<int:part_id>', methods=['GET'])
def get_spare_part(part_id):
    spare_part = spare_part_controller.get_spare_part_by_id(part_id)
    if spare_part:
        return make_response(jsonify(spare_part), HTTPStatus.OK)
    return make_response("Spare Part not found", HTTPStatus.NOT_FOUND)

@spare_part_bp.route('', methods=['POST'])
def create_spare_part():
    content = request.get_json()
    spare_part = spare_part_controller.create_spare_part(content)
    return make_response(jsonify(spare_part), HTTPStatus.CREATED)

@spare_part_bp.route('/<int:part_id>', methods=['PUT'])
def update_spare_part(part_id: int):
    content = request.get_json()
    updated_spare_part = spare_part_controller.update_spare_part(part_id, content)
    if updated_spare_part:
        return make_response(jsonify(updated_spare_part), HTTPStatus.OK)
    return make_response("Spare Part not found", HTTPStatus.NOT_FOUND)

@spare_part_bp.route('/<int:part_id>', methods=['DELETE'])
def delete_spare_part(part_id: int):
    result = spare_part_controller.delete_spare_part(part_id)
    if result:
        return make_response("Spare Part deleted", HTTPStatus.OK)
    return make_response("Spare Part not found", HTTPStatus.NOT_FOUND)


@spare_part_bp.route('/aggregated_quantities', methods=['GET'])
def get_aggregated_quantities():
    aggregated_quantities = spare_part_controller.get_aggregated_quantities()
    return jsonify(aggregated_quantities)
