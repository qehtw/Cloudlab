from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from flasgger import swag_from
from ..controllers.technician_schedule_controller import TechnicianSchedulesController

technician_schedule_bp = Blueprint('technician_schedule', __name__, url_prefix='/technician_schedule')

@technician_schedule_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Technician Schedules'],
    'responses': {
        200: {
            'description': 'List of all technician schedules',
            'examples': {
                'application/json': [
                    {'schedule_id': 1, 'technician_id': 1, 'date': '2025-10-08', 'time': '09:00'}
                ]
            }
        }
    }
})
def get_all_technician_schedules():
    schedules = TechnicianSchedulesController.get_all_schedules()
    return make_response(jsonify(schedules), HTTPStatus.OK)

@technician_schedule_bp.route('/<int:schedule_id>', methods=['GET'])
@swag_from({
    'tags': ['Technician Schedules'],
    'parameters': [
        {'name': 'schedule_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the schedule'}
    ],
    'responses': {
        200: {'description': 'Schedule found', 'examples': {'application/json': {'schedule_id': 1, 'technician_id': 1}}},
        404: {'description': 'Schedule not found'}
    }
})
def get_technician_schedule(schedule_id):
    schedule = TechnicianSchedulesController.get_schedule_by_id(schedule_id)
    if schedule:
        return make_response(jsonify(schedule), HTTPStatus.OK)
    return make_response("Schedule not found", HTTPStatus.NOT_FOUND)

@technician_schedule_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Technician Schedules'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'technician_id': {'type': 'integer'},
                    'date': {'type': 'string', 'format': 'date'},
                    'time': {'type': 'string', 'format': 'time'}
                },
                'required': ['technician_id', 'date', 'time']
            }
        }
    ],
    'responses': {
        201: {'description': 'Schedule created'},
        400: {'description': 'Invalid input'}
    }
})
def create_technician_schedule():
    content = request.get_json()
    schedule = TechnicianSchedulesController.create_schedule(content)
    return make_response(jsonify(schedule), HTTPStatus.CREATED)

@technician_schedule_bp.route('/<int:schedule_id>', methods=['PUT'])
@swag_from({
    'tags': ['Technician Schedules'],
    'parameters': [
        {'name': 'schedule_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the schedule'},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'technician_id': {'type': 'integer'},
                    'date': {'type': 'string', 'format': 'date'},
                    'time': {'type': 'string', 'format': 'time'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Schedule updated'},
        404: {'description': 'Schedule not found'}
    }
})
def update_technician_schedule(schedule_id: int):
    content = request.get_json()
    updated_schedule = TechnicianSchedulesController.update_schedule(schedule_id, content)
    if updated_schedule:
        return make_response(jsonify(updated_schedule), HTTPStatus.OK)
    return make_response("Schedule not found", HTTPStatus.NOT_FOUND)

@technician_schedule_bp.route('/<int:schedule_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Technician Schedules'],
    'parameters': [
        {'name': 'schedule_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the schedule'}
    ],
    'responses': {
        200: {'description': 'Schedule deleted'},
        404: {'description': 'Schedule not found'}
    }
})
def delete_technician_schedule(schedule_id: int):
    result = TechnicianSchedulesController.delete_schedule(schedule_id)
    if result:
        return make_response("Technician Schedule deleted", HTTPStatus.OK)
    return make_response("Schedule not found", HTTPStatus.NOT_FOUND)
