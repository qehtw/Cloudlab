from app.models.repair_type import RepairType
from app.database import db

class RepairTypeService:
    @staticmethod
    def find_all():
        return RepairType.query.all()

    @staticmethod
    def find_by_id(repair_type_id: int):
        return RepairType.query.get(repair_type_id)

    @staticmethod
    def create(repair_type: RepairType):
        db.session.add(repair_type)
        db.session.commit()

    @staticmethod
    def update(repair_type: RepairType):
        db.session.commit()

    @staticmethod
    def delete(repair_type_id: int):
        repair_type = RepairTypeService.find_by_id(repair_type_id)
        if repair_type:
            db.session.delete(repair_type)
            db.session.commit()


