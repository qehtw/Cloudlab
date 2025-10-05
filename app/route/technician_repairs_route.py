from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from ..controllers import technician_repairs_controller

technician_repairs_bp = Blueprint('technician_repairs', __name__, url_prefix='/technician_repairs')

@technician_repairs_bp.route('', methods=['GET'])
def get_all_technician_repairs():
    technician_repairs = technician_repairs_controller.get_all_technician_repairs()
    return make_response(jsonify(technician_repairs), HTTPStatus.OK)

@technician_repairs_bp.route('/<int:technician_repair_id>', methods=['GET'])
def get_technician_repair(technician_repair_id):
    technician_repair = technician_repairs_controller.get_technician_repair_by_id(technician_repair_id)
    if technician_repair:
        return make_response(jsonify(technician_repair), HTTPStatus.OK)
    return make_response("Technician Repair not found", HTTPStatus.NOT_FOUND)

@technician_repairs_bp.route('', methods=['POST'])
def create_technician_repair():
    content = request.get_json()
    technician_repair = technician_repairs_controller.create_technician_repair(content)
    if technician_repair:
        return make_response(jsonify(technician_repair), HTTPStatus.CREATED)
    return make_response({"error": "Technician or Repair not found"}, HTTPStatus.BAD_REQUEST)

@technician_repairs_bp.route('/<int:technician_repair_id>', methods=['DELETE'])
def delete_technician_repair(technician_repair_id: int):
    result = technician_repairs_controller.delete_technician_repair(technician_repair_id)
    if result:
        return make_response("Technician Repair deleted", HTTPStatus.OK)
    return make_response("Technician Repair not found", HTTPStatus.NOT_FOUND)
