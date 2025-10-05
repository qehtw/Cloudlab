from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from ..controllers.technician_controller import TechniciansController

technician_bp = Blueprint('technician', __name__, url_prefix='/technician')

@technician_bp.route('', methods=['GET'])
def get_all_technicians():
    technicians = TechniciansController.get_all_technicians()
    return make_response(jsonify(technicians), HTTPStatus.OK)

@technician_bp.route('/<int:technician_id>', methods=['GET'])
def get_technician(technician_id):
    technician = TechniciansController.get_technician_by_id(technician_id)
    if technician:
        return make_response(jsonify(technician), HTTPStatus.OK)
    return make_response("Technician not found", HTTPStatus.NOT_FOUND)

@technician_bp.route('', methods=['POST'])
def create_technician():
    content = request.get_json()
    technician = TechniciansController.create_technician(content)
    return make_response(jsonify(technician), HTTPStatus.CREATED)

@technician_bp.route('/<int:technician_id>', methods=['PUT'])
def update_technician(technician_id: int):
    content = request.get_json()
    updated_technician = TechniciansController.update_technician(technician_id, content)
    if updated_technician:
        return make_response(jsonify(updated_technician), HTTPStatus.OK)
    return make_response("Technician not found", HTTPStatus.NOT_FOUND)

@technician_bp.route('/<int:technician_id>', methods=['DELETE'])
def delete_technician(technician_id: int):
    result = TechniciansController.delete_technician(technician_id)
    if result:
        return make_response("Technician deleted", HTTPStatus.OK)
    return make_response("Technician not found", HTTPStatus.NOT_FOUND)
