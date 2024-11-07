from sqlalchemy.orm import Session
from models.models import User
from sqlalchemy.exc import SQLAlchemyError
from services.service import Service

class UserService(Service):
    def __init__(self, engine):
        super().__init__(engine)

    def create(self, data):
        try:
            with Session(self.engine) as session:
                new_user = User(
                    username=data.get('username'),
                    password=data.get('password'),
                    role=data.get('role', 'user')
                )
                session.add(new_user)
                session.commit()
                return new_user.to_json()
        except SQLAlchemyError as e:
            session.rollback()
            return e
 
    def update(self, user_id, data):
        try:
            with Session(self.engine) as session:
                user = session.get(User, user_id)

                for key, value in data.items():
                    if (hasattr(user, key)):
                        setattr(user, key, value)
                
                session.commit()
                return user.to_json()
        except SQLAlchemyError as e:
            session.rollback()
            return e
        
    def delete(self, user_id):
        try:
            with Session(self.engine) as session:
                user = session.get(User, user_id)
                if not user:
                    return None
                
                session.delete(user)
                session.commit()
                return {"Code": "OK"}
        except SQLAlchemyError as e:
            session.rollback()
            return e

    def get_all(self):
        try:
            with Session(self.engine) as session:
                users = session.query(User).all()
                return users
        except SQLAlchemyError as e:
            return e