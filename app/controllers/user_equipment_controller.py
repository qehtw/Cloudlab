# app/controllers/user_equipment_controller.py
from app.models.user_equipment import UserEquipment
from app.services.user_equipment_service import UserEquipmentService
from .general_controller import GeneralController

class UserEquipmentController(GeneralController):
    @staticmethod
    def get_all_user_equipment():
        return [user_equipment.to_dict() for user_equipment in UserEquipmentService.find_all()]

    @staticmethod
    def get_user_equipment_by_id(user_equipment_id: int):
        user_equipment = UserEquipmentService.find_by_id(user_equipment_id)
        return user_equipment.to_dict() if user_equipment else None

    @staticmethod
    def create_user_equipment(user_equipment_data: dict):
        user_equipment = UserEquipment.create_from_dto(user_equipment_data)
        UserEquipmentService.create(user_equipment)
        return user_equipment.to_dict()

    @staticmethod
    def update_user_equipment(user_equipment_id: int, user_equipment_data: dict):
        user_equipment = UserEquipmentService.find_by_id(user_equipment_id)
        if user_equipment:
            user_equipment.update_from_dto(user_equipment_data)
            UserEquipmentService.update(user_equipment)
            return user_equipment.to_dict()
        return None

    @staticmethod
    def delete_user_equipment(user_equipment_id: int):
        UserEquipmentService.delete(user_equipment_id)
        return {"message": "User equipment deleted successfully"}
