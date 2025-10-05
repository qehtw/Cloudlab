from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controllers import equipment_controller

equipment_bp = Blueprint('equipment', __name__, url_prefix='/equipment')

@equipment_bp.route('', methods=['GET'])
def get_all_equipment() -> Response:
    equipment = equipment_controller.get_all_equipment()
    return make_response(jsonify(equipment), HTTPStatus.OK)

@equipment_bp.route('/<int:equipment_id>', methods=['GET'])
def get_equipment(equipment_id: int) -> Response:
    return make_response(jsonify(equipment_controller.get_equipment(equipment_id)), HTTPStatus.OK)

@equipment_bp.route('', methods=['POST'])
def create_equipment() -> Response:
    content = request.get_json()
    equipment = equipment_controller.create_equipment(content)
    return make_response(jsonify(equipment), HTTPStatus.CREATED)

@equipment_bp.route('/<int:equipment_id>', methods=['PUT'])
def update_equipment(equipment_id: int) -> Response:
    content = request.get_json()
    updated_equipment = equipment_controller.update_equipment(equipment_id, content)
    return make_response(jsonify(updated_equipment), HTTPStatus.OK)

@equipment_bp.route('/<int:equipment_id>', methods=['DELETE'])
def delete_equipment(equipment_id: int) -> Response:
    equipment_controller.delete_equipment(equipment_id)
    return make_response("Equipment deleted", HTTPStatus.OK)
