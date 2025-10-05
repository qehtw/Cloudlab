# app/models/repair_type.py
from app.database import db

class RepairType(db.Model):
    __tablename__ = 'repair_types'

    repair_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    repairs = db.relationship('Repair', back_populates='repair_type')

    def to_dict(self):
        return {
            'repair_type_id': self.repair_type_id,
            'name': self.name,
        }
