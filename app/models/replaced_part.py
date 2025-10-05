# app/models/replaced_part.py
from app.database import db

class ReplacedPart(db.Model):
    __tablename__ = 'replaced_parts'

    replaced_part_id = db.Column(db.Integer, primary_key=True)
    repair_id = db.Column(db.Integer, db.ForeignKey('repairs.repair_id'))
    part_id = db.Column(db.Integer, db.ForeignKey('spare_parts.part_id'))
    quantity = db.Column(db.Integer, nullable=False)

    repair = db.relationship('Repair', back_populates='replaced_parts')
    part = db.relationship('SparePart', back_populates='replaced_parts')

    def to_dict(self):
        return {
            'replaced_part_id': self.replaced_part_id,
            'repair_id': self.repair_id,
            'part_id': self.part_id,
            'quantity': self.quantity,
            'repair': self.repair.to_dict_basic() if self.repair else None,
            'part': self.part.to_dict() if self.part else None
        }
