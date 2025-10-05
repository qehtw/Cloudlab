from app.models.equipment import Equipment
from app.database import db

class EquipmentDAO:

    @staticmethod
    def get_all():
        return Equipment.query.all()

    @staticmethod
    def get_by_id(equipment_id: int):
        return Equipment.query.get(equipment_id)

    @staticmethod
    def create(data):
        new_equipment = Equipment(
            name=data['name'],
            manufacturer_id=data['manufacturer_id']
        )
        db.session.add(new_equipment)
        db.session.commit()
        return new_equipment

    @staticmethod
    def update(equipment_id: int, data):
        equipment = Equipment.query.get(equipment_id)
        if equipment:
            equipment.name = data.get('name', equipment.name)
            equipment.manufacturer_id = data.get('manufacturer_id', equipment.manufacturer_id)
            db.session.commit()
        return equipment

    @staticmethod
    def delete(equipment_id: int):
        equipment = Equipment.query.get(equipment_id)
        if equipment:
            db.session.delete(equipment)
            db.session.commit()
        return equipment
