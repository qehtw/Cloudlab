from app.models.equipment import Equipment
from app.services.equipment_service import EquipmentService
from .general_controller import GeneralController
from http import HTTPStatus

class EquipmentController(GeneralController):
    @staticmethod
    def get_all_equipment():
        equipment = EquipmentService.get_all_equipment()
        return [equip.to_dict() for equip in equipment]

    @staticmethod
    def get_equipment_by_id(equipment_id: int):
        equipment = EquipmentService.get_equipment_by_id(equipment_id)
        return equipment.to_dict() if equipment else {"error": "Equipment not found"}, HTTPStatus.NOT_FOUND

    @staticmethod
    def create_equipment(data: dict):
        equipment = Equipment.create_from_dto(data)
        EquipmentService.create_equipment(equipment)
        return equipment.to_dict()

    @staticmethod
    def update_equipment(equipment_id: int, data: dict):
        equipment = EquipmentService.get_equipment_by_id(equipment_id)
        if equipment:
            equipment.update_from_dto(data)
            EquipmentService.update_equipment(equipment)
            return equipment.to_dict()
        return {"error": "Equipment not found"}, HTTPStatus.NOT_FOUND

    @staticmethod
    def delete_equipment(equipment_id: int):
        equipment = EquipmentService.get_equipment_by_id(equipment_id)
        if equipment:
            EquipmentService.delete_equipment(equipment_id)
            return {"message": "Equipment deleted successfully"}
        return {"error": "Equipment not found"}, HTTPStatus.NOT_FOUND
