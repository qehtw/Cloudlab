from app.models.technician_repairs import TechnicianRepairs
from app.services.technician_repairs_service import TechnicianRepairsService
from .general_controller import GeneralController

class TechnicianRepairsController(GeneralController):
    @staticmethod
    def get_all_technician_repairs():
        return [technician_repair.to_dict() for technician_repair in TechnicianRepairsService.find_all()]

    @staticmethod
    def get_technician_repair_by_id(technician_repair_id: int):
        technician_repair = TechnicianRepairsService.find_by_id(technician_repair_id)
        return technician_repair.to_dict() if technician_repair else None

    @staticmethod
    def create_technician_repair(technician_repair_data: dict):
        # Отримуємо імена техніка та ремонту
        technician_name = technician_repair_data.get("technician_name")
        repair_name = technician_repair_data.get("repair_name")

        # Створення запису через DTO
        technician_repair = TechnicianRepairs.create_from_dto({
            "technician_name": technician_name,
            "repair_name": repair_name
        })

        # Якщо створено, зберігаємо в базі
        if technician_repair:
            TechnicianRepairsService.create(technician_repair)
            return technician_repair.to_dict()
        return None  # Якщо технік чи ремонт не знайдено

    @staticmethod
    def delete_technician_repair(technician_repair_id: int):
        technician_repair = TechnicianRepairsService.find_by_id(technician_repair_id)
        if technician_repair:
            TechnicianRepairsService.delete(technician_repair)
            return True
        return False
