# app/controllers/repairs_controller.py
from app.models.repair import Repair
from app.services.repair_service import RepairService
from .general_controller import GeneralController

class RepairsController(GeneralController):
    @staticmethod
    def get_all_repairs():
        return [repair.to_dict() for repair in RepairService.find_all()]

    @staticmethod
    def get_repair_by_id(repair_id: int):
        repair = RepairService.find_by_id(repair_id)
        return repair.to_dict() if repair else None

    @staticmethod
    def create_repair(repair_data: dict):
        repair = Repair.create_from_dto(repair_data)
        RepairService.create(repair)
        return repair.to_dict()

    @staticmethod
    def update_repair(repair_id: int, repair_data: dict):
        repair = RepairService.find_by_id(repair_id)
        if repair:
            repair.update_from_dto(repair_data)
            RepairService.update(repair)
            return repair.to_dict()
        return None

    @staticmethod
    def delete_repair(repair_id: int):
        RepairService.delete(repair_id)
        return {"message": "Repair deleted successfully"}
