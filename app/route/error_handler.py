from http import HTTPStatus
from flask import Blueprint, Response, make_response, jsonify

err_handler_bp = Blueprint('errors', __name__)

@err_handler_bp.app_errorhandler(HTTPStatus.NOT_FOUND)
def handle_404(error: int) -> Response:
    return make_response(jsonify({"error": "Object not found"}), HTTPStatus.NOT_FOUND)

@err_handler_bp.app_errorhandler(HTTPStatus.UNPROCESSABLE_ENTITY)
def handle_422(error: int) -> Response:
    return make_response(jsonify({"error": "Input data is wrong or not full"}), HTTPStatus.UNPROCESSABLE_ENTITY)

@err_handler_bp.app_errorhandler(HTTPStatus.CONFLICT)
def handle_409(error: int) -> Response:
    return make_response(jsonify({"error": "Such object already exists in DB"}), HTTPStatus.CONFLICT)

@err_handler_bp.app_errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def handle_500(error: int) -> Response:
    return make_response(jsonify({"error": "Internal server error"}), HTTPStatus.INTERNAL_SERVER_ERROR)