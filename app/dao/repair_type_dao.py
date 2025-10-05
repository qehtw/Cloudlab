# app/dao/repair_type_dao.py
from ..models.repair_type import RepairType
from app.database import db

class RepairTypeDAO:
    @staticmethod
    def get_all_repair_types():
        return RepairType.query.all()

    @staticmethod
    def get_repair_type(repair_type_id):
        return RepairType.query.get(repair_type_id)

    @staticmethod
    def create_repair_type(data):
        repair_type = RepairType(**data)
        db.session.add(repair_type)
        db.session.commit()
        return repair_type

    @staticmethod
    def update_repair_type(repair_type_id, data):
        repair_type = RepairTypeDAO.get_repair_type(repair_type_id)
        for key, value in data.items():
            setattr(repair_type, key, value)
        db.session.commit()
        return repair_type

    @staticmethod
    def delete_repair_type(repair_type_id):
        repair_type = RepairTypeDAO.get_repair_type(repair_type_id)
        db.session.delete(repair_type)
        db.session.commit()
