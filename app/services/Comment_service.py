from app.models.Comments import Comment
from app.database import db

class CommentService:
    @staticmethod
    def find_all():
        return Comment.query.all()

    @staticmethod
    def find_by_id(comment_id: int):
        return Comment.query.get(comment_id)

    @staticmethod
    def create(comment: Comment):
        db.session.add(comment)
        db.session.commit()

    @staticmethod
    def update(comment: Comment):
        db.session.commit()

    @staticmethod
    def delete(comment_id: int):
        comment = CommentService.find_by_id(comment_id)
        if comment:
            db.session.delete(comment)
            db.session.commit()
