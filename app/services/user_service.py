from app import db
from app.models.user import User

class UserService:
    @staticmethod
    def find_all():
        return User.query.all()

    @staticmethod
    def find_by_id(user_id: int):
        return User.query.get(user_id)

    @staticmethod
    def create(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def update(user):
        db.session.commit()

    @staticmethod
    def delete(user_id: int):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
