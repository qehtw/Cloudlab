from app.database import db
from app.models.manufacturer import Manufacturer
from app.database import db
import random
import string
from datetime import datetime
from sqlalchemy import text


class ManufacturerService:
    @staticmethod
    def find_all():
        """Отримати всіх виробників"""
        return Manufacturer.query.all()

    @staticmethod
    def find_by_id(manufacturer_id: int):
        """Знайти виробника за ID"""
        return Manufacturer.query.get(manufacturer_id)

    @staticmethod
    def create(manufacturer: Manufacturer):
        """Створення нового виробника"""
        db.session.add(manufacturer)
        db.session.commit()

    @staticmethod
    def update(manufacturer: Manufacturer):
        """Оновлення виробника"""
        db.session.commit()

    @staticmethod
    def delete(manufacturer_id: int):
        """Видалення виробника"""
        manufacturer = ManufacturerService.find_by_id(manufacturer_id)
        if manufacturer:
            db.session.delete(manufacturer)
            db.session.commit()

    @staticmethod
    def generate_random_string(length=8):
        """Генерація випадкового рядка для імені стовпця чи таблиці"""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def create_dynamic_tables():
        """
        Динамічно створює таблиці на основі записів зі стовпця `name` таблиці `Manufacturers`.
        Генерується випадкове ім'я для таблиці та випадкові стовпці з випадковими типами даних.
        """
        # Отримуємо всі записи зі стовпця `name` таблиці `Manufacturers`
        manufacturers = db.session.query(Manufacturer.name).all()

        # Лічильник створених таблиць
        table_count = 0

        for manufacturer in manufacturers:
            if table_count >= 10:  # обмежуємо кількість таблиць
                break

            manufacturer_name = manufacturer[0].replace(" ", "_")  # Замінюємо пробіли на "_"
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            table_name = f"{manufacturer_name}_{timestamp}"

            # Генерація випадкової кількості стовпців (від 1 до 9)
            num_columns = random.randint(1, 9)

            # Генерація стовпців з випадковими іменами та типами даних
            columns_sql = []
            for i in range(1, num_columns + 1):
                col_name = ManufacturerService.generate_random_string()
                col_type = random.choice(["VARCHAR(255)", "INT", "DECIMAL(10,2)", "DATE"])
                columns_sql.append(f"{col_name} {col_type}")

            columns_sql_str = ", ".join(columns_sql)
            create_table_sql = f"CREATE TABLE `{table_name}` (id INT AUTO_INCREMENT PRIMARY KEY, {columns_sql_str});"

            # Виконання SQL для створення таблиці
            db.session.execute(text(create_table_sql))
            print(f"Created table: {table_name}")

            # Збільшення лічильника створених таблиць
            table_count += 1

        db.session.commit()
