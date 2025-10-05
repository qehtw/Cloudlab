# app/controllers/repair_types_controller.py
from app.models.repair_type import RepairType
from app.services.repair_type_service import RepairTypeService
from .general_controller import GeneralController

class RepairTypesController(GeneralController):
    @staticmethod
    def get_all_repair_types():
        return [repair_type.to_dict() for repair_type in RepairTypeService.find_all()]

    @staticmethod
    def get_repair_type_by_id(repair_type_id: int):
        repair_type = RepairTypeService.find_by_id(repair_type_id)
        return repair_type.to_dict() if repair_type else None

    @staticmethod
    def create_repair_type(repair_type_data: dict):
        repair_type = RepairType.create_from_dto(repair_type_data)
        RepairTypeService.create(repair_type)
        return repair_type.to_dict()

    @staticmethod
    def update_repair_type(repair_type_id: int, repair_type_data: dict):
        repair_type = RepairTypeService.find_by_id(repair_type_id)
        if repair_type:
            repair_type.update_from_dto(repair_type_data)
            RepairTypeService.update(repair_type)
            return repair_type.to_dict()
        return None

    @staticmethod
    def delete_repair_type(repair_type_id: int):
        RepairTypeService.delete(repair_type_id)
        return {"message": "Repair type deleted successfully"}
