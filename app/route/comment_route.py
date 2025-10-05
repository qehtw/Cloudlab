from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from ..controllers import commentsController

comment_bp = Blueprint('comment', __name__, url_prefix='/comment')

@comment_bp.route('', methods=['GET'])
def get_all_comments():
    comments = commentsController.get_all_comments()  # Виправлено
    return make_response(jsonify(comments), HTTPStatus.OK)

@comment_bp.route('/<int:comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = commentsController.get_comment_by_id(comment_id)  # Виправлено
    if comment:
        return make_response(jsonify(comment), HTTPStatus.OK)
    return make_response("Comment not found", HTTPStatus.NOT_FOUND)

@comment_bp.route('', methods=['POST'])
def create_comment():
    content = request.get_json()
    comment = commentsController.create_comment(content)  # Виправлено
    return make_response(jsonify(comment), HTTPStatus.CREATED)

@comment_bp.route('/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id: int):
    content = request.get_json()
    updated_comment = commentsController.update_comment(comment_id, content)  # Виправлено
    if updated_comment:
        return make_response(jsonify(updated_comment), HTTPStatus.OK)
    return make_response("Comment not found", HTTPStatus.NOT_FOUND)

@comment_bp.route('/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id: int):
    result = commentsController.delete_comment(comment_id)  # Виправлено
    if result:
        return make_response("Comment deleted", HTTPStatus.OK)
    return make_response("Comment not found", HTTPStatus.NOT_FOUND)
