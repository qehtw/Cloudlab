from app.database import db

class Repair(db.Model):
    __tablename__ = 'repairs'

    repair_id = db.Column(db.Integer, primary_key=True)
    user_equipment_id = db.Column(db.Integer, db.ForeignKey('user_equipment.user_equipment_id'))
    repair_type_id = db.Column(db.Integer, db.ForeignKey('repair_types.repair_type_id'))
    status = db.Column(db.Enum('in_progress', 'completed'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)
    repairs_name = db.Column(db.String(255), nullable=True)  # Додаємо нову колонку для імені ремонту

    user_equipment = db.relationship('UserEquipment', back_populates='repairs')
    repair_type = db.relationship('RepairType', back_populates='repairs')
    technicians = db.relationship('Technician', secondary='technician_repairs', back_populates='repairs')
    replaced_parts = db.relationship('ReplacedPart', back_populates='repair')
    comments = db.relationship('Comment', back_populates='repair', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'repair_id': self.repair_id,
            'user_equipment_id': self.user_equipment_id,
            'repair_type_id': self.repair_type_id,
            'status': self.status,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'repairs_name': self.repairs_name,  # Додаємо поле repairs_name в метод to_dict
            'user_equipment': self.user_equipment.to_dict() if self.user_equipment else None,
            'repair_type': self.repair_type.to_dict() if self.repair_type else None,
            'comments': [comment.to_dict() for comment in self.comments]
        }

    def to_dict_basic(self):
        return {
            'repair_id': self.repair_id,
            'user_equipment_id': self.user_equipment_id,
            'repair_type_id': self.repair_type_id,
            'status': self.status,
            'repairs_name': self.repairs_name,  # Додаємо поле repairs_name в метод to_dict_basic
        }

