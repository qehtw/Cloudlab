# app/controllers/spare_parts_controller.py
from app.models.spare_part import SparePart
from app.services.spare_part_service import SparePartService
from .general_controller import GeneralController

class SparePartsController(GeneralController):
    @staticmethod
    def get_all_spare_parts():
        return [spare_part.to_dict() for spare_part in SparePartService.find_all()]

    @staticmethod
    def get_spare_part_by_id(spare_part_id: int):
        spare_part = SparePartService.find_by_id(spare_part_id)
        return spare_part.to_dict() if spare_part else None

    @staticmethod
    def create_spare_part(spare_part_data: dict):
        spare_part = SparePart.create_from_dto(spare_part_data)
        SparePartService.create(spare_part)
        return spare_part.to_dict()

    @staticmethod
    def update_spare_part(spare_part_id: int, spare_part_data: dict):
        spare_part = SparePartService.find_by_id(spare_part_id)
        if spare_part:
            spare_part.update_from_dto(spare_part_data)
            SparePartService.update(spare_part)
            return spare_part.to_dict()
        return None

    @staticmethod
    def delete_spare_part(spare_part_id: int):
        SparePartService.delete(spare_part_id)
        return {"message": "Spare part deleted successfully"}


    @staticmethod
    def get_aggregated_quantities():
        return SparePartService.get_aggregated_quantities()
