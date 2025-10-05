# app/dao/user_equipment_dao.py
from ..models.user_equipment import UserEquipment
from app.database import db

class UserEquipmentDAO:
    @staticmethod
    def get_all_user_equipment():
        return UserEquipment.query.all()

    @staticmethod
    def get_user_equipment(user_equipment_id):
        return UserEquipment.query.get(user_equipment_id)

    @staticmethod
    def create_user_equipment(data):
        user_equipment = UserEquipment(**data)
        db.session.add(user_equipment)
        db.session.commit()
        return user_equipment

    @staticmethod
    def update_user_equipment(user_equipment_id, data):
        user_equipment = UserEquipmentDAO.get_user_equipment(user_equipment_id)
        for key, value in data.items():
            setattr(user_equipment, key, value)
        db.session.commit()
        return user_equipment

    @staticmethod
    def delete_user_equipment(user_equipment_id):
        user_equipment = UserEquipmentDAO.get_user_equipment(user_equipment_id)
        db.session.delete(user_equipment)
        db.session.commit()
