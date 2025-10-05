# app/dao/user_dao.py
from ..models.user import User
from app.database import db

class UserDAO:
    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user(user_id):
        return User.query.get(user_id)

    @staticmethod
    def create_user(data):
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def update_user(user_id, data):
        user = UserDAO.get_user(user_id)
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        user = UserDAO.get_user(user_id)
        db.session.delete(user)
        db.session.commit()
