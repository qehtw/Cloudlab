# app/models/technician_schedule.py
from app.database import db

class TechnicianSchedule(db.Model):
    __tablename__ = 'technician_schedule'

    schedule_id = db.Column(db.Integer, primary_key=True)
    technician_id = db.Column(db.Integer, db.ForeignKey('technicians.technician_id'))
    work_day = db.Column(db.Enum('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'))
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)

    technician = db.relationship('Technician', back_populates='schedule')

    def to_dict(self):
        return {
            'schedule_id': self.schedule_id,
            'technician_id': self.technician_id,
            'work_day': self.work_day,
            'start_time': self.start_time.isoformat() if self.start_time else None,
            'end_time': self.end_time.isoformat() if self.end_time else None,
            'technician': self.technician.to_dict() if self.technician else None
        }
