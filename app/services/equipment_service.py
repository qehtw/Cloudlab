from ..dao.equipment_dao import EquipmentDAO

class EquipmentService:

    @staticmethod
    def get_all_equipment():
        return EquipmentDAO.get_all()

    @staticmethod
    def get_equipment_by_id(equipment_id: int):
        return EquipmentDAO.get_by_id(equipment_id)

    @staticmethod
    def create_equipment(data):
        return EquipmentDAO.create(data)

    @staticmethod
    def update_equipment(equipment_id: int, data):
        return EquipmentDAO.update(equipment_id, data)

    @staticmethod
    def delete_equipment(equipment_id: int):
        return EquipmentDAO.delete(equipment_id)
