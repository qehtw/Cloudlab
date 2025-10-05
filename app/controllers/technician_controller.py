# app/controllers/technicians_controller.py
from app.models.technician import Technician
from app.services.technician_service import TechnicianService
from .general_controller import GeneralController

class TechniciansController(GeneralController):
    @staticmethod
    def get_all_technicians():
        return [technician.to_dict() for technician in TechnicianService.find_all()]

    @staticmethod
    def get_technician_by_id(technician_id: int):
        technician = TechnicianService.find_by_id(technician_id)
        return technician.to_dict() if technician else None

    @staticmethod
    def create_technician(technician_data: dict):
        technician = Technician.create_from_dto(technician_data)
        TechnicianService.create(technician)
        return technician.to_dict()

    @staticmethod
    def update_technician(technician_id: int, technician_data: dict):
        technician = TechnicianService.find_by_id(technician_id)
        if technician:
            technician.update_from_dto(technician_data)
            TechnicianService.update(technician)
            return technician.to_dict()
        return None

    @staticmethod
    def delete_technician(technician_id: int):
        TechnicianService.delete(technician_id)
        return {"message": "Technician deleted successfully"}
