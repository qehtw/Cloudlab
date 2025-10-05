from app.models.spare_part import SparePart
from app.database import db
from sqlalchemy import func

class SparePartService:
    @staticmethod
    def find_all():
        return SparePart.query.all()

    @staticmethod
    def find_by_id(part_id: int):
        return SparePart.query.get(part_id)

    @staticmethod
    def create(spare_part: SparePart):
        db.session.add(spare_part)
        db.session.commit()

    @staticmethod
    def update(spare_part: SparePart):
        db.session.commit()

    @staticmethod
    def delete(part_id: int):
        spare_part = SparePartService.find_by_id(part_id)
        if spare_part:
            db.session.delete(spare_part)
            db.session.commit()

    @staticmethod
    def get_aggregated_quantities():
        """
        Отримати мінімальне, максимальне, сумарне та середнє значення для стовпця `quantity` таблиці `SpareParts`.
        """
        result = db.session.query(
            func.min(SparePart.quantity).label('min_quantity'),
            func.max(SparePart.quantity).label('max_quantity'),
            func.sum(SparePart.quantity).label('sum_quantity'),
            func.avg(SparePart.quantity).label('avg_quantity')
        ).first()  # Використовуємо `first()`, щоб отримати перший (і єдиний) результат

        if result:
            return {
                'min_quantity': result.min_quantity,
                'max_quantity': result.max_quantity,
                'sum_quantity': result.sum_quantity,
                'avg_quantity': result.avg_quantity
            }
        return None  # Якщо результату немає


