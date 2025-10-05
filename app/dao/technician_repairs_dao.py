from ..models.technician_repairs import TechnicianRepairs
from app.database import db

class TechnicianRepairsDAO:
    @staticmethod
    def get_all_technician_repairs():
        return TechnicianRepairs.query.all()

    @staticmethod
    def get_technician_repair(technician_id, repair_id):
        return TechnicianRepairs.query.filter_by(technician_id=technician_id, repair_id=repair_id).first()

    @staticmethod
    def create_technician_repair(data):
        repair = TechnicianRepairs(**data)
        db.session.add(repair)
        db.session.commit()
        return repair

    @staticmethod
    def update_technician_repair(technician_id, repair_id, data):
        repair = TechnicianRepairs.query.filter_by(technician_id=technician_id, repair_id=repair_id).first()
        if repair:
            for key, value in data.items():
                setattr(repair, key, value)
            db.session.commit()
        return repair

    @staticmethod
    def delete_technician_repair(technician_id, repair_id):
        repair = TechnicianRepairs.query.filter_by(technician_id=technician_id, repair_id=repair_id).first()
        if repair:
            db.session.delete(repair)
            db.session.commit()

    @staticmethod
    def get_repairs_by_technician(technician_id):
        # Приклад використання ORM (SQLAlchemy)
        return TechnicianRepairs.query.filter_by(technician_id=technician_id).all()

