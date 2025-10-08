from flask import Blueprint, jsonify, request, make_response
from flasgger import swag_from
from app.controllers.manufacturer_controller import ManufacturersController

manufacturer_bp = Blueprint('manufacturer', __name__, url_prefix='/manufacturer')

@manufacturer_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Manufacturer'],
    'responses': {
        200: {
            'description': 'List of all manufacturers',
            'examples': {
                'application/json': [
                    {'manufacturer_id': 1, 'name': 'Sony'},
                    {'manufacturer_id': 2, 'name': 'Samsung'}
                ]
            }
        }
    }
})
def get_all_manufacturers():
    manufacturers = ManufacturersController.get_all_manufacturers()
    return make_response(jsonify(manufacturers), 200)

@manufacturer_bp.route('/<int:manufacturer_id>', methods=['GET'])
@swag_from({
    'tags': ['Manufacturer'],
    'parameters': [
        {'name': 'manufacturer_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the manufacturer'}
    ],
    'responses': {
        200: {'description': 'Manufacturer found', 'examples': {'application/json': {'manufacturer_id': 1, 'name': 'Sony'}}},
        404: {'description': 'Manufacturer not found'}
    }
})
def get_manufacturer_route(manufacturer_id):
    manufacturer = ManufacturersController.get_manufacturer_by_id(manufacturer_id)
    if manufacturer:
        return make_response(jsonify(manufacturer), 200)
    return make_response("Manufacturer not found", 404)

@manufacturer_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Manufacturer'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'}
                },
                'required': ['name']
            }
        }
    ],
    'responses': {
        201: {'description': 'Manufacturer created', 'examples': {'application/json': {'manufacturer_id': 3, 'name': 'LG'}}}
    }
})
def create_manufacturer():
    content = request.get_json()
    manufacturer = ManufacturersController.create_manufacturer(content)
    return make_response(jsonify(manufacturer), 201)

@manufacturer_bp.route('/<int:manufacturer_id>', methods=['PUT'])
@swag_from({
    'tags': ['Manufacturer'],
    'parameters': [
        {'name': 'manufacturer_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the manufacturer'},
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Manufacturer updated'},
        404: {'description': 'Manufacturer not found'}
    }
})
def update_manufacturer(manufacturer_id):
    content = request.get_json()
    updated_manufacturer = ManufacturersController.update_manufacturer(manufacturer_id, content)
    if updated_manufacturer:
        return make_response(jsonify(updated_manufacturer), 200)
    return make_response("Manufacturer not found", 404)

@manufacturer_bp.route('/<int:manufacturer_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Manufacturer'],
    'parameters': [
        {'name': 'manufacturer_id', 'in': 'path', 'type': 'integer', 'required': True, 'description': 'ID of the manufacturer'}
    ],
    'responses': {
        200: {'description': 'Manufacturer deleted'},
        404: {'description': 'Manufacturer not found'}
    }
})
def delete_manufacturer(manufacturer_id):
    result = ManufacturersController.delete_manufacturer(manufacturer_id)
    if result:
        return make_response("Manufacturer deleted", 200)
    return make_response("Manufacturer not found", 404)

@manufacturer_bp.route('/create', methods=['POST'])
@swag_from({
    'tags': ['Manufacturer'],
    'responses': {
        201: {'description': '10 manufacturers added successfully'},
        500: {'description': 'Server error'}
    }
})
def create_manufacturer_entries():
    try:
        ManufacturersController.create_manufacturer_entries()
        return make_response(jsonify({"message": "10 manufacturers have been added."}), 201)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

@manufacturer_bp.route('/create_dynamic_tables', methods=['POST'])
@swag_from({
    'tags': ['Manufacturer'],
    'responses': {
        200: {'description': 'Dynamic tables created successfully'},
        500: {'description': 'Server error'}
    }
})
def create_dynamic_tables():
    try:
        ManufacturersController.create_dynamic_tables()
        return jsonify({"message": "Dynamic tables created successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
