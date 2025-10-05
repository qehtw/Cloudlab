# app/controllers/comments_controller.py
from app.models.Comments import Comment
from app.services.Comment_service import CommentService
from .general_controller import GeneralController

class CommentsController(GeneralController):  # Виправлено ім'я класу
    @staticmethod
    def get_all_comments():
        return [comment.to_dict() for comment in CommentService.find_all()]

    @staticmethod
    def get_comment_by_id(comment_id: int):
        comment = CommentService.find_by_id(comment_id)
        return comment.to_dict() if comment else None

    @staticmethod
    def create_comment(comment_data: dict):
        comment = Comment.create_from_dto(comment_data)
        CommentService.create(comment)
        return comment.to_dict()

    @staticmethod
    def update_comment(comment_id: int, comment_data: dict):
        comment = CommentService.find_by_id(comment_id)
        if comment:
            comment.update_from_dto(comment_data)
            CommentService.update(comment)
            return comment.to_dict()
        return None

    @staticmethod
    def delete_comment(comment_id: int):
        CommentService.delete(comment_id)
        return {"message": "Comment deleted successfully"}
