# app/models/user_equipment.py
from app.database import db

class UserEquipment(db.Model):
    __tablename__ = 'user_equipment'

    user_equipment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.equipment_id'))
    serial_number = db.Column(db.String(255))
    purchase_date = db.Column(db.Date)

    user = db.relationship('User', back_populates='equipment')
    equipment = db.relationship('Equipment', back_populates='user_equipment')
    repairs = db.relationship('Repair', back_populates='user_equipment')

    def to_dict(self):
        return {
            'user_equipment_id': self.user_equipment_id,
            'user_id': self.user_id,
            'equipment_id': self.equipment_id,
            'serial_number': self.serial_number,
            'purchase_date': self.purchase_date.isoformat() if self.purchase_date else None,
            'user': self.user.to_dict() if self.user else None,
            'equipment': self.equipment.to_dict() if self.equipment else None
        }
