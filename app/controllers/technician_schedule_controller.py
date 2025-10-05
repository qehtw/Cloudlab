# app/controllers/technician_schedules_controller.py
from app.models.technician_schedule import TechnicianSchedule
from app.services.technician_schedule_service import TechnicianScheduleService
from .general_controller import GeneralController

class TechnicianSchedulesController(GeneralController):
    @staticmethod
    def get_all_schedules():
        return [schedule.to_dict() for schedule in TechnicianScheduleService.find_all()]

    @staticmethod
    def get_schedule_by_id(schedule_id: int):
        schedule = TechnicianScheduleService.find_by_id(schedule_id)
        return schedule.to_dict() if schedule else None

    @staticmethod
    def create_schedule(schedule_data: dict):
        schedule = TechnicianSchedule.create_from_dto(schedule_data)
        TechnicianScheduleService.create(schedule)
        return schedule.to_dict()

    @staticmethod
    def update_schedule(schedule_id: int, schedule_data: dict):
        schedule = TechnicianScheduleService.find_by_id(schedule_id)
        if schedule:
            schedule.update_from_dto(schedule_data)
            TechnicianScheduleService.update(schedule)
            return schedule.to_dict()
        return None

    @staticmethod
    def delete_schedule(schedule_id: int):
        TechnicianScheduleService.delete(schedule_id)
        return {"message": "Technician schedule deleted successfully"}
