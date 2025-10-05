# app/models/equipment.py
from app.database import db

class Equipment(db.Model):
    __tablename__ = 'equipment'

    equipment_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturers.manufacturer_id'))

    manufacturer = db.relationship('Manufacturer', back_populates='equipment')
    user_equipment = db.relationship('UserEquipment', back_populates='equipment')

    def to_dict(self):
        return {
            'equipment_id': self.equipment_id,
            'name': self.name,
            'manufacturer_id': self.manufacturer_id,
        }
