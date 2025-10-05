from app.models.technician import Technician
from app.database import db

class TechnicianService:
    @staticmethod
    def find_all():
        return Technician.query.all()

    @staticmethod
    def find_by_id(technician_id: int):
        return Technician.query.get(technician_id)

    @staticmethod
    def create(technician: Technician):
        db.session.add(technician)
        db.session.commit()

    @staticmethod
    def update(technician: Technician):
        db.session.commit()

    @staticmethod
    def delete(technician_id: int):
        technician = TechnicianService.find_by_id(technician_id)
        if technician:
            db.session.delete(technician)
            db.session.commit()
