from app.models.replaced_part import ReplacedPart
from app.database import db

class ReplacedPartService:
    @staticmethod
    def find_all():
        return ReplacedPart.query.all()

    @staticmethod
    def find_by_id(replaced_part_id: int):
        return ReplacedPart.query.get(replaced_part_id)

    @staticmethod
    def create(replaced_part: ReplacedPart):
        db.session.add(replaced_part)
        db.session.commit()

    @staticmethod
    def update(replaced_part: ReplacedPart):
        db.session.commit()

    @staticmethod
    def delete(replaced_part_id: int):
        replaced_part = ReplacedPartService.find_by_id(replaced_part_id)
        if replaced_part:
            db.session.delete(replaced_part)
            db.session.commit()



