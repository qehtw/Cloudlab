# app/dao/manufacturer_dao.py
from ..models.manufacturer import Manufacturer
from app.database import db

class ManufacturerDAO:
    @staticmethod
    def get_all_manufacturers():
        return Manufacturer.query.all()

    @staticmethod
    def get_manufacturer(manufacturer_id):
        return Manufacturer.query.get(manufacturer_id)

    @staticmethod
    def create_manufacturer(data):
        manufacturer = Manufacturer(**data)
        db.session.add(manufacturer)
        db.session.commit()
        return manufacturer

    @staticmethod
    def update_manufacturer(manufacturer_id, data):
        manufacturer = ManufacturerDAO.get_manufacturer(manufacturer_id)
        for key, value in data.items():
            setattr(manufacturer, key, value)
        db.session.commit()
        return manufacturer

    @staticmethod
    def delete_manufacturer(manufacturer_id):
        manufacturer = ManufacturerDAO.get_manufacturer(manufacturer_id)
        db.session.delete(manufacturer)
        db.session.commit()
