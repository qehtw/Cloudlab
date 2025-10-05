from app.models.Comments import Comment
from app.database import db

class CommentDAO:
    @staticmethod
    def get_comments_by_repair_id(repair_id: int):
        return Comment.query.filter_by(repair_id=repair_id).all()

    @staticmethod
    def get_comment_by_id(comment_id: int):
        return Comment.query.get(comment_id)

    @staticmethod
    def create_comment(repair_id: int, comment_text: str):
        comment = Comment(repair_id=repair_id, comment=comment_text)
        db.session.add(comment)
        db.session.commit()
        return comment

    @staticmethod
    def update_comment(comment_id: int, new_comment_text: str):
        comment = Comment.query.get(comment_id)
        if comment:
            comment.comment = new_comment_text
            db.session.commit()
        return comment

    @staticmethod
    def delete_comment(comment_id: int):
        comment = Comment.query.get(comment_id)
        if comment:
            db.session.delete(comment)
            db.session.commit()
        return comment
