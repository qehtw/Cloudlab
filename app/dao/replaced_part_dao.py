# app/dao/replaced_part_dao.py
from ..models.replaced_part import ReplacedPart
from app.database import db

class ReplacedPartDAO:
    @staticmethod
    def get_all_replaced_parts():
        return ReplacedPart.query.all()

    @staticmethod
    def get_replaced_part(replaced_part_id):
        return ReplacedPart.query.get(replaced_part_id)

    @staticmethod
    def create_replaced_part(data):
        replaced_part = ReplacedPart(**data)
        db.session.add(replaced_part)
        db.session.commit()
        return replaced_part

    @staticmethod
    def update_replaced_part(replaced_part_id, data):
        replaced_part = ReplacedPartDAO.get_replaced_part(replaced_part_id)
        for key, value in data.items():
            setattr(replaced_part, key, value)
        db.session.commit()
        return replaced_part

    @staticmethod
    def delete_replaced_part(replaced_part_id):
        replaced_part = ReplacedPartDAO.get_replaced_part(replaced_part_id)
        db.session.delete(replaced_part)
        db.session.commit()
