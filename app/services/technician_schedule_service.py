from app.models.technician_schedule import TechnicianSchedule
from app.database import db

class TechnicianScheduleService:
    @staticmethod
    def find_all():
        return TechnicianSchedule.query.all()

    @staticmethod
    def find_by_id(schedule_id: int):
        return TechnicianSchedule.query.get(schedule_id)

    @staticmethod
    def create(schedule: TechnicianSchedule):
        db.session.add(schedule)
        db.session.commit()

    @staticmethod
    def update(schedule: TechnicianSchedule):
        db.session.commit()

    @staticmethod
    def delete(schedule_id: int):
        schedule = TechnicianScheduleService.find_by_id(schedule_id)
        if schedule:
            db.session.delete(schedule)
            db.session.commit()
