from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from flasgger import swag_from
from ..controllers import commentsController

comment_bp = Blueprint('comment', __name__, url_prefix='/comment')

@comment_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Comments'],
    'responses': {
        200: {
            'description': 'List of all comments',
            'examples': {
                'application/json': [
                    {'comment_id': 1, 'text': 'Great post!', 'user_id': 2},
                    {'comment_id': 2, 'text': 'Thanks for sharing', 'user_id': 3}
                ]
            }
        }
    }
})
def get_all_comments():
    comments = commentsController.get_all_comments()
    return make_response(jsonify(comments), HTTPStatus.OK)

@comment_bp.route('/<int:comment_id>', methods=['GET'])
@swag_from({
    'tags': ['Comments'],
    'parameters': [
        {
            'name': 'comment_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the comment'
        }
    ],
    'responses': {
        200: {
            'description': 'Comment found',
            'examples': {'application/json': {'comment_id': 1, 'text': 'Great post!', 'user_id': 2}}
        },
        404: {'description': 'Comment not found'}
    }
})
def get_comment(comment_id):
    comment = commentsController.get_comment_by_id(comment_id)
    if comment:
        return make_response(jsonify(comment), HTTPStatus.OK)
    return make_response("Comment not found", HTTPStatus.NOT_FOUND)

@comment_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Comments'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'text': {'type': 'string'},
                    'user_id': {'type': 'integer'}
                },
                'required': ['text', 'user_id']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Comment created',
            'examples': {'application/json': {'comment_id': 3, 'text': 'New comment', 'user_id': 1}}
        }
    }
})
def create_comment():
    content = request.get_json()
    comment = commentsController.create_comment(content)
    return make_response(jsonify(comment), HTTPStatus.CREATED)

@comment_bp.route('/<int:comment_id>', methods=['PUT'])
@swag_from({
    'tags': ['Comments'],
    'parameters': [
        {'name': 'comment_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the comment'},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {'text': {'type': 'string'}}
            }
        }
    ],
    'responses': {
        200: {'description': 'Comment updated'},
        404: {'description': 'Comment not found'}
    }
})
def update_comment(comment_id: int):
    content = request.get_json()
    updated_comment = commentsController.update_comment(comment_id, content)
    if updated_comment:
        return make_response(jsonify(updated_comment), HTTPStatus.OK)
    return make_response("Comment not found", HTTPStatus.NOT_FOUND)

@comment_bp.route('/<int:comment_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Comments'],
    'parameters': [
        {'name': 'comment_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the comment'}
    ],
    'responses': {
        200: {'description': 'Comment deleted'},
        404: {'description': 'Comment not found'}
    }
})
def delete_comment(comment_id: int):
    result = commentsController.delete_comment(comment_id)
    if result:
        return make_response("Comment deleted", HTTPStatus.OK)
    return make_response("Comment not found", HTTPStatus.NOT_FOUND)
