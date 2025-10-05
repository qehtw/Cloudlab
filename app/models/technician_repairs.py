from app.database import db
from typing import Dict, Any
from app.models.technician import Technician
from app.models.repair import Repair


class TechnicianRepairs(db.Model):
    __tablename__ = 'technician_repairs'

    technician_repair_id = db.Column(db.Integer, primary_key=True)
    technician_id = db.Column(db.Integer, db.ForeignKey('technicians.technician_id'), nullable=False)
    repair_id = db.Column(db.Integer, db.ForeignKey('repairs.repair_id'), nullable=False)

    technician = db.relationship('Technician', backref='technician_repairs')
    repair = db.relationship('Repair', backref='technician_repairs')

    def to_dict(self):
        return {
            "technician_name": self.technician.name if self.technician else None,  # Показуємо ім'я техніка
            "repair_name": self.repair.repairs_name if self.repair else None  # Показуємо ім'я ремонту
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'TechnicianRepairs':
        # Замість передачі ID, отримуємо техніка і ремонт за їх іменами
        technician_name = dto_dict.get("technician_name")
        repair_name = dto_dict.get("repair_name")

        technician = Technician.query.filter_by(name=technician_name).first()
        repair = Repair.query.filter_by(repairs_name=repair_name).first()

        if technician and repair:
            # Якщо технік та ремонт знайдені, створюємо запис у таблиці
            return TechnicianRepairs(
                technician_id=technician.technician_id,
                repair_id=repair.repair_id,
            )
        return None  # Якщо не знайдено, повертаємо None
