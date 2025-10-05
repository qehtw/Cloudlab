from abc import ABC
from typing import List, Dict, Optional, Any
from http import HTTPStatus
from flask import abort

class GeneralController(ABC):
    _service = None

    def find_all(self) -> List[Dict[str, Any]]:
        # Виконуємо `put_into_dto()` тільки якщо об'єкт має цей метод
        return [
            item.put_into_dto() if hasattr(item, 'put_into_dto') else item
            for item in self._service.find_all()
        ]

    def find_by_id(self, key: int) -> Dict[str, Any]:
        # Знайти об'єкт за ідентифікатором або повернути помилку
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        # Виконуємо `put_into_dto()` тільки якщо об'єкт має цей метод
        return obj.put_into_dto() if hasattr(obj, 'put_into_dto') else obj

    def create(self, obj: object) -> Dict[str, Any]:
        # Створення нового об'єкта і перевірка, чи він має метод `put_into_dto`
        created_obj = self._service.create(obj)
        if hasattr(created_obj, 'put_into_dto'):
            return created_obj.put_into_dto()
        else:
            return created_obj

    def create_all(self, obj_list: List[object]) -> List[Dict[str, Any]]:
        # Створення кількох об'єктів і повернення їх DTO, якщо можливо
        created_objects = self._service.create_all(obj_list)
        return [
            item.put_into_dto() if hasattr(item, 'put_into_dto') else item
            for item in created_objects
        ]

    def update(self, key: int, new_obj: object) -> None:
        # Оновлення існуючого об'єкта
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        self._service.update(key, new_obj)

    def patch(self, key: int, value_dict: Dict[str, Any]) -> None:
        """Часткове оновлення, передаючи словник з оновленнями."""
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        self._service.patch(key, value_dict)

    def delete(self, key: int) -> None:
        # Видалення об'єкта за ідентифікатором
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        self._service.delete(key)

    def delete_all(self) -> None:
        # Видалення всіх об'єктів
        self._service.delete_all()

    def get_related_data(self, key: int, relation_name: str) -> List[Dict[str, Any]]:
        # Отримання зв'язаних даних для об'єкта
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)

        related_data = getattr(obj, relation_name, None)
        if related_data is None:
            abort(HTTPStatus.NOT_FOUND)

        # Перевірка, чи це колекція об'єктів або один об'єкт
        if isinstance(related_data, list) or hasattr(related_data, '__iter__'):
            return [
                item.put_into_dto() if hasattr(item, 'put_into_dto') else item
                for item in related_data
            ]
        else:
            return related_data.put_into_dto() if hasattr(related_data, 'put_into_dto') else related_data

    def add_related_data(self, key: int, related_obj: object, relation_name: str) -> None:
        # Додавання зв'язаних даних до об'єкта
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)

        related_collection = getattr(obj, relation_name, None)
        if related_collection is None or not hasattr(related_collection, 'append'):
            abort(HTTPStatus.BAD_REQUEST, "Неможливо додати дані до цієї колекції")

        related_collection.append(related_obj)
        self._service.update(key, obj)

    def put(self, key1: int, key2: int, new_data: dict):
        """
        Оновлення об'єкта через сервісний шар.
        """
        return self._service.put(key1, key2, new_data)