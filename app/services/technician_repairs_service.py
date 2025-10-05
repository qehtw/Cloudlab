from app.models.technician_repairs import TechnicianRepairs
from app.database import db

class TechnicianRepairsService:
    @staticmethod
    def find_all():
        return TechnicianRepairs.query.all()

    @staticmethod
    def find_by_id(technician_repair_id: int):
        return TechnicianRepairs.query.get(technician_repair_id)

    @staticmethod
    def create(technician_repair: TechnicianRepairs):
        db.session.add(technician_repair)
        db.session.commit()

    @staticmethod
    def delete(technician_repair_id: int):
        technician_repair = TechnicianRepairsService.find_by_id(technician_repair_id)
        if technician_repair:
            db.session.delete(technician_repair)
            db.session.commit()
