from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from ..controllers.technician_schedule_controller import TechnicianSchedulesController

technician_schedule_bp = Blueprint('technician_schedule', __name__, url_prefix='/technician_schedule')

@technician_schedule_bp.route('', methods=['GET'])
def get_all_technician_schedules():
    schedules = TechnicianSchedulesController.get_all_schedules()
    return make_response(jsonify(schedules), HTTPStatus.OK)

@technician_schedule_bp.route('/<int:schedule_id>', methods=['GET'])
def get_technician_schedule(schedule_id):
    schedule = TechnicianSchedulesController.get_all_schedules()
    if schedule:
        return make_response(jsonify(schedule), HTTPStatus.OK)
    return make_response("Schedule not found", HTTPStatus.NOT_FOUND)

@technician_schedule_bp.route('', methods=['POST'])
def create_technician_schedule():
    content = request.get_json()
    schedule = TechnicianSchedulesController.create_schedule(content)
    return make_response(jsonify(schedule), HTTPStatus.CREATED)

@technician_schedule_bp.route('/<int:schedule_id>', methods=['PUT'])
def update_technician_schedule(schedule_id: int):
    content = request.get_json()
    updated_schedule = TechnicianSchedulesController.update_schedule(schedule_id, content)
    if updated_schedule:
        return make_response(jsonify(updated_schedule), HTTPStatus.OK)
    return make_response("Schedule not found", HTTPStatus.NOT_FOUND)

@technician_schedule_bp.route('/<int:schedule_id>', methods=['DELETE'])
def delete_technician_schedule(schedule_id: int):
    TechnicianSchedulesController.delete_schedule(schedule_id)
    return make_response("Technician Schedule deleted", HTTPStatus.OK)
