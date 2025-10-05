from app.models.user_equipment import UserEquipment
from app.database import db

class UserEquipmentService:
    @staticmethod
    def find_all():
        return UserEquipment.query.all()

    @staticmethod
    def find_by_id(user_equipment_id: int):
        return UserEquipment.query.get(user_equipment_id)

    @staticmethod
    def create(user_equipment: UserEquipment):
        db.session.add(user_equipment)
        db.session.commit()

    @staticmethod
    def update(user_equipment: UserEquipment):
        db.session.commit()

    @staticmethod
    def delete(user_equipment_id: int):
        user_equipment = UserEquipmentService.find_by_id(user_equipment_id)
        if user_equipment:
            db.session.delete(user_equipment)
            db.session.commit()
