from app.models.repair import Repair
from app.database import db

class RepairDAO:
    @staticmethod
    def get_all_repairs():
        return Repair.query.all()

    @staticmethod
    def get_repair_by_id(repair_id: int):
        return Repair.query.get(repair_id)

    @staticmethod
    def create_repair(user_equipment_id, repair_type_id, status, start_date, end_date=None):
        repair = Repair(
            user_equipment_id=user_equipment_id,
            repair_type_id=repair_type_id,
            status=status,
            start_date=start_date,
            end_date=end_date
        )
        db.session.add(repair)
        db.session.commit()
        return repair

    @staticmethod
    def update_repair(repair_id: int, status=None, end_date=None):
        repair = Repair.query.get(repair_id)
        if repair:
            if status:
                repair.status = status
            if end_date:
                repair.end_date = end_date
            db.session.commit()
        return repair

    @staticmethod
    def delete_repair(repair_id: int):
        repair = Repair.query.get(repair_id)
        if repair:
            db.session.delete(repair)
            db.session.commit()
        return repair
