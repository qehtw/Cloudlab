import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from app.config import Config
from app.route import register_routes
from app.database import db
import mysql.connector

print(sys.path)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    register_routes(app)

    with app.app_context():
        print("Таблиці вже існують або створені.")

    return app


def create_database():
    """Створюємо базу даних, якщо її ще немає"""
    connection = mysql.connector.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
    )
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Config.DB_NAME}")
    cursor.close()
    connection.close()
    print(f"База даних {Config.DB_NAME} готова.")


def create_tables(app):
    """Створюємо таблиці лише якщо вони відсутні"""
    with app.app_context():
        inspector = inspect(db.engine)
        existing_tables = inspector.get_table_names()

        # Перелік моделей та їхніх таблиць
        metadata = db.Model.metadata
        for table_name, table_obj in metadata.tables.items():
            if table_name not in existing_tables:
                print(f"Створюємо таблицю {table_name}...")
                table_obj.create(db.engine)
            else:
                print(f"Таблиця {table_name} вже існує, пропускаємо.")


def populate_data():
    """Вставка даних з SQL файлу, без дублювання"""
    sql_file_path = os.path.abspath('data.sql')
    if not os.path.exists(sql_file_path):
        print("SQL файл не знайдений за шляхом:", sql_file_path)
        return

    connection = mysql.connector.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME
    )
    cursor = connection.cursor()

    with open(sql_file_path, 'r') as sql_file:
        sql_text = sql_file.read()
        sql_statements = sql_text.split(';')
        for statement in sql_statements:
            statement = statement.strip()
            if statement:
                try:
                    # Використовуємо IGNORE, щоб уникнути помилок дублювання
                    cursor.execute(statement)
                    connection.commit()
                except mysql.connector.Error as error:
                    print(f"Помилка при виконанні SQL: {error}")
                    connection.rollback()

    cursor.close()
    connection.close()
    print("Дані вставлені або вже існували.")

app = create_app()
