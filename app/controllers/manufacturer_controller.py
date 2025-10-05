from app.models.manufacturer import Manufacturer
from app.services.manufacturer_service import ManufacturerService
from .general_controller import GeneralController
from app.database import db

class ManufacturersController(GeneralController):
    @staticmethod
    def get_all_manufacturers():
        return [manufacturer.to_dict() for manufacturer in ManufacturerService.find_all()]

    @staticmethod
    def get_manufacturer_by_id(manufacturer_id: int):
        manufacturer = ManufacturerService.find_by_id(manufacturer_id)
        return manufacturer.to_dict() if manufacturer else None

    @staticmethod
    def create_manufacturer(manufacturer_data: dict):
        manufacturer = Manufacturer.create_from_dto(manufacturer_data)
        ManufacturerService.create(manufacturer)
        return manufacturer.to_dict()

    @staticmethod
    def update_manufacturer(manufacturer_id: int, manufacturer_data: dict):
        manufacturer = ManufacturerService.find_by_id(manufacturer_id)
        if manufacturer:
            # Оновлення атрибутів вручну
            manufacturer.name = manufacturer_data.get('name', manufacturer.name)
            # Якщо є інші поля, додавайте їх так:
            # manufacturer.other_field = manufacturer_data.get('other_field', manufacturer.other_field)

            ManufacturerService.update(manufacturer)
            return manufacturer.to_dict()
        return None

    @staticmethod
    def delete_manufacturer(manufacturer_id: int):
        ManufacturerService.delete(manufacturer_id)
        return {"message": "Manufacturer deleted successfully"}

    @staticmethod
    def create_manufacturer_entries():
        """
        Створює 10 записів у таблиці manufacturers з назвами у форматі 'Noname1', 'Noname2', ..., 'Noname10'
        """
        for i in range(1, 11):
            manufacturer_name = f"Noname{i}"

            # Створюємо новий запис
            new_manufacturer = Manufacturer(name=manufacturer_name)

            # Додаємо його в сесію
            db.session.add(new_manufacturer)

        # Зберігаємо зміни в базі даних
        db.session.commit()

        print("10 manufacturers have been added.")

    @staticmethod
    def create_dynamic_tables():
        """
        Викликає метод для динамічного створення таблиць на основі записів зі стовпця `name` таблиці `Manufacturers`.
        Генерується випадкове ім'я для таблиці та випадкові стовпці з випадковими типами даних.
        """
        try:
            # Викликаємо метод з сервісу для створення таблиць
            ManufacturerService.create_dynamic_tables()  
            return {"message": "Dynamic tables created successfully."}, 200
        except Exception as e:
            # Якщо сталася помилка, повертаємо повідомлення про помилку
            return {"error": str(e)}, 500
