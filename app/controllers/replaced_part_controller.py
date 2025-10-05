# app/controllers/replaced_parts_controller.py
from app.models.replaced_part import ReplacedPart
from app.services.replaced_part_service import ReplacedPartService
from .general_controller import GeneralController

class ReplacedPartsController(GeneralController):
    @staticmethod
    def get_all_replaced_parts():
        return [replaced_part.to_dict() for replaced_part in ReplacedPartService.find_all()]

    @staticmethod
    def get_replaced_part_by_id(replaced_part_id: int):
        replaced_part = ReplacedPartService.find_by_id(replaced_part_id)
        return replaced_part.to_dict() if replaced_part else None

    @staticmethod
    def create_replaced_part(replaced_part_data: dict):
        replaced_part = ReplacedPart.create_from_dto(replaced_part_data)
        ReplacedPartService.create(replaced_part)
        return replaced_part.to_dict()

    @staticmethod
    def update_replaced_part(replaced_part_id: int, replaced_part_data: dict):
        replaced_part = ReplacedPartService.find_by_id(replaced_part_id)
        if replaced_part:
            replaced_part.update_from_dto(replaced_part_data)
            ReplacedPartService.update(replaced_part)
            return replaced_part.to_dict()
        return None

    @staticmethod
    def delete_replaced_part(replaced_part_id: int):
        ReplacedPartService.delete(replaced_part_id)
        return {"message": "Replaced part deleted successfully"}
