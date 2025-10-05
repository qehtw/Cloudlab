# app/dao/spare_part_dao.py
from ..models.spare_part import SparePart
from app.database import db

class SparePartDAO:
    @staticmethod
    def get_all_spare_parts():
        return SparePart.query.all()

    @staticmethod
    def get_spare_part(spare_part_id):
        return SparePart.query.get(spare_part_id)

    @staticmethod
    def create_spare_part(data):
        spare_part = SparePart(**data)
        db.session.add(spare_part)
        db.session.commit()
        return spare_part

    @staticmethod
    def update_spare_part(spare_part_id, data):
        spare_part = SparePartDAO.get_spare_part(spare_part_id)
        for key, value in data.items():
            setattr(spare_part, key, value)
        db.session.commit()
        return spare_part

    @staticmethod
    def delete_spare_part(spare_part_id):
        spare_part = SparePartDAO.get_spare_part(spare_part_id)
        db.session.delete(spare_part)
        db.session.commit()
