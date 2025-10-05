from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from ..controllers.user_equipment_controller import UserEquipmentController

user_equipment_bp = Blueprint('user_equipment', __name__, url_prefix='/user_equipment')

@user_equipment_bp.route('', methods=['GET'])
def get_all_user_equipment():
    user_equipment = UserEquipmentController.get_all_user_equipment()
    return make_response(jsonify(user_equipment), HTTPStatus.OK)

@user_equipment_bp.route('/<int:user_equipment_id>', methods=['GET'])
def get_user_equipment(user_equipment_id: int):
    user_equipment = UserEquipmentController.get_user_equipment_by_id(user_equipment_id)
    if user_equipment:
        return make_response(jsonify(user_equipment), HTTPStatus.OK)
    return make_response("User equipment not found", HTTPStatus.NOT_FOUND)

@user_equipment_bp.route('', methods=['POST'])
def create_user_equipment():
    content = request.get_json()
    user_equipment = UserEquipmentController.create_user_equipment(content)
    return make_response(jsonify(user_equipment), HTTPStatus.CREATED)

@user_equipment_bp.route('/<int:user_equipment_id>', methods=['PUT'])
def update_user_equipment(user_equipment_id: int):
    content = request.get_json()
    updated_user_equipment = UserEquipmentController.update_user_equipment(user_equipment_id, content)
    if updated_user_equipment:
        return make_response(jsonify(updated_user_equipment), HTTPStatus.OK)
    return make_response("User equipment not found", HTTPStatus.NOT_FOUND)

@user_equipment_bp.route('/<int:user_equipment_id>', methods=['DELETE'])
def delete_user_equipment(user_equipment_id: int):
    UserEquipmentController.delete_user_equipment(user_equipment_id)
    return make_response("User equipment deleted", HTTPStatus.OK)
