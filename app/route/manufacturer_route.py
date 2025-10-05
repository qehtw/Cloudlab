# app/routes/manufacturer_routes.py
from flask import Blueprint, jsonify, request, make_response
from app.controllers.manufacturer_controller import ManufacturersController

manufacturer_bp = Blueprint('manufacturer', __name__, url_prefix='/manufacturer')

@manufacturer_bp.route('', methods=['GET'])
def get_all_manufacturers():
    manufacturers = ManufacturersController.get_all_manufacturers()
    return make_response(jsonify(manufacturers), 200)

@manufacturer_bp.route('/<int:manufacturer_id>', methods=['GET'])
def get_manufacturer_route(manufacturer_id):
    manufacturer = ManufacturersController.get_manufacturer_by_id(manufacturer_id)
    if manufacturer:
        return make_response(jsonify(manufacturer), 200)
    return make_response("Manufacturer not found", 404)

@manufacturer_bp.route('', methods=['POST'])
def create_manufacturer():
    content = request.get_json()
    manufacturer = ManufacturersController.create_manufacturer(content)
    return make_response(jsonify(manufacturer), 201)

@manufacturer_bp.route('/<int:manufacturer_id>', methods=['PUT'])
def update_manufacturer(manufacturer_id: int):
    content = request.get_json()
    updated_manufacturer = ManufacturersController.update_manufacturer(manufacturer_id, content)
    if updated_manufacturer:
        return make_response(jsonify(updated_manufacturer), 200)
    return make_response("Manufacturer not found", 404)

@manufacturer_bp.route('/<int:manufacturer_id>', methods=['DELETE'])
def delete_manufacturer(manufacturer_id: int):
    ManufacturersController.delete_manufacturer(manufacturer_id)
    return make_response("Manufacturer deleted", 200)


@manufacturer_bp.route('/create', methods=['POST'])
def create_manufacturer_entries():
    try:
        ManufacturersController.create_manufacturer_entries()  # Викликаємо сервіс для створення записів
        return make_response(jsonify({"message": "10 manufacturers have been added."}), 201)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)


@manufacturer_bp.route('/create_dynamic_tables', methods=['POST'])
def create_dynamic_tables():
    """
    Викликає метод для динамічного створення таблиць на основі записів зі стовпця `name` таблиці `Manufacturers`.
    """
    try:
        ManufacturersController.create_dynamic_tables()  # Викликає метод з сервісу для створення таблиць
        return jsonify({"message": "Dynamic tables created successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
