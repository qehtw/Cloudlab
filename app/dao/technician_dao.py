# app/dao/technician_dao.py
from ..models.technician import Technician
from app.database import db

class TechnicianDAO:
    @staticmethod
    def get_all_technicians():
        return Technician.query.all()

    @staticmethod
    def get_technician(technician_id):
        return Technician.query.get(technician_id)

    @staticmethod
    def create_technician(data):
        technician = Technician(**data)
        db.session.add(technician)
        db.session.commit()
        return technician

    @staticmethod
    def update_technician(technician_id, data):
        technician = TechnicianDAO.get_technician(technician_id)
        for key, value in data.items():
            setattr(technician, key, value)
        db.session.commit()
        return technician

    @staticmethod
    def delete_technician(technician_id):
        technician = TechnicianDAO.get_technician(technician_id)
        db.session.delete(technician)
        db.session.commit()
