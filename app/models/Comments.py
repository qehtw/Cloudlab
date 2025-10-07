from __future__ import annotations
from typing import Dict, Any
from app import db
from sqlalchemy import event, select

class Comment(db.Model):
    __tablename__ = 'repair_comments'

    comment_id = db.Column(db.Integer, primary_key=True)
    repair_id = db.Column(db.Integer, db.ForeignKey('repairs.repair_id', ondelete='CASCADE'))  # Зовнішній ключ на repairs
    comment = db.Column(db.Text, nullable=False)

    # Відношення до Repair
    repair = db.relationship('Repair', back_populates='comments')

    def __repr__(self):
        return f"Comment(comment_id={self.comment_id}, repair_id={self.repair_id}, comment={self.comment}, created_at={self.created_at})"

    def to_dict(self):
        return {
            "comment_id": self.comment_id,
            "repair_id": self.repair_id,
            "comment": self.comment,
        }

    @staticmethod
    def create_from_dto(dto_dict):
        return Comment(
            repair_id=dto_dict.get('repair_id'),
            comment=dto_dict.get('comment'),
            created_at=dto_dict.get('created_at')
        )

# Перевірка перед вставкою для перевірки на існування запису в таблиці repairs
@event.listens_for(Comment, "before_insert")
def check_repair_exists(mapper, connection, target):
    repair_table = db.Table('repairs', db.metadata, autoload_with=db.engine)

    repair_exists = connection.execute(
        select(repair_table.c.repair_id).where(repair_table.c.repair_id == target.repair_id)
    ).first()

    if not repair_exists:
        raise ValueError(f"Repair with id {target.repair_id} does not exist in repairs table.")
