from app.models.user import User
from app.services.user_service import UserService
from .general_controller import GeneralController

class UsersController(GeneralController):
    @staticmethod
    def get_all_users():
        """Отримати всіх користувачів"""
        return [user.to_dict() for user in UserService.find_all()]

    @staticmethod
    def get_user(user_id):
        """Отримати користувача за ID"""
        # Пошук користувача за id
        user = User.query.get(user_id)
        if user:
            return user.to_dict()  # Повертати словник з даними користувача
        return None

    @staticmethod
    def get_user_by_id(user_id: int):
        """Отримати користувача за ID з використанням сервісу"""
        user = UserService.find_by_id(user_id)
        return user.to_dict() if user else None

    @staticmethod
    def create_user(user_data: dict):
        """Створити нового користувача"""
        user = User.create_from_dto(user_data)
        UserService.create(user)
        return user.to_dict()

    @staticmethod
    def update_user(user_id: int, user_data: dict):
        """Оновити дані користувача за ID"""
        user = UserService.find_by_id(user_id)
        if user:
            user.update_from_dto(user_data)
            UserService.update(user)
            return user.to_dict()
        return None

    @staticmethod
    def delete_user(user_id: int):
        """Видалити користувача за ID"""
        UserService.delete(user_id)
        return {"message": "User deleted successfully"}
