from ..models.technician_schedule import TechnicianSchedule
from app.database import db

class TechnicianScheduleDAO:
    @staticmethod
    def get_all_schedules():
        return TechnicianSchedule.query.all()

    @staticmethod
    def get_schedule(schedule_id):
        return TechnicianSchedule.query.get(schedule_id)

    @staticmethod
    def create_schedule(data):
        schedule = TechnicianSchedule(**data)
        db.session.add(schedule)
        db.session.commit()
        return schedule

    @staticmethod
    def update_schedule(schedule_id, data):
        schedule = TechnicianSchedule.query.get(schedule_id)
        if schedule:
            for key, value in data.items():
                setattr(schedule, key, value)
            db.session.commit()
        return schedule

    @staticmethod
    def delete_schedule(schedule_id):
        schedule = TechnicianSchedule.query.get(schedule_id)
        if schedule:
            db.session.delete(schedule)
            db.session.commit()
