from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from ..controllers import repair_controller

repair_bp = Blueprint('repair', __name__, url_prefix='/repair')

@repair_bp.route('', methods=['GET'])
def get_all_repairs():
    repairs = repair_controller.get_all_repairs()
    return make_response(jsonify(repairs), HTTPStatus.OK)

@repair_bp.route('/<int:repair_id>', methods=['GET'])
def get_repair(repair_id):
    repair = repair_controller.get_repair_by_id(repair_id)
    if repair:
        return make_response(jsonify(repair), HTTPStatus.OK)
    return make_response("Repair not found", HTTPStatus.NOT_FOUND)

@repair_bp.route('', methods=['POST'])
def create_repair():
    content = request.get_json()
    repair = repair_controller.create_repair(content)
    return make_response(jsonify(repair), HTTPStatus.CREATED)

@repair_bp.route('/<int:repair_id>', methods=['PUT'])
def update_repair(repair_id: int):
    content = request.get_json()
    updated_repair = repair_controller.update_repair(repair_id, content)
    if updated_repair:
        return make_response(jsonify(updated_repair), HTTPStatus.OK)
    return make_response("Repair not found", HTTPStatus.NOT_FOUND)

@repair_bp.route('/<int:repair_id>', methods=['DELETE'])
def delete_repair(repair_id: int):
    result = repair_controller.delete_repair(repair_id)
    if result:
        return make_response("Repair deleted", HTTPStatus.OK)
    return make_response("Repair not found", HTTPStatus.NOT_FOUND)
