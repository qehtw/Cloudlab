from app.models.repair import Repair
from app.database import db

class RepairService:
    @staticmethod
    def find_all():
        return Repair.query.all()

    @staticmethod
    def find_by_id(repair_id: int):
        return Repair.query.get(repair_id)

    @staticmethod
    def create(repair: Repair):
        db.session.add(repair)
        db.session.commit()

    @staticmethod
    def update(repair: Repair):
        db.session.commit()

    @staticmethod
    def delete(repair_id: int):
        repair = RepairService.find_by_id(repair_id)
        if repair:
            db.session.delete(repair)
            db.session.commit()
