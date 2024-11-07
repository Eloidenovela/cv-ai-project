from sqlalchemy.orm import Session
from models.models import Presences
from sqlalchemy.exc import SQLAlchemyError
from services.service import Service

class PresencesService(Service):
    def __init__(self, engine):
        super().__init__(engine)

    def create(self, data):
        try:
            with Session(self.engine) as session:
                new_presence = Presences(
                    employee_id=data.get('employee_id'),
                    date=data.get('date'),
                    presences=data.get('presences'),
                    absences=data.get('absences')
                )
                session.add(new_presence)
                session.commit()
                return new_presence.to_json()
        except SQLAlchemyError as e:
            session.rollback()
            return e

    def update(self, presence_id, data):
        try:
            with Session(self.engine) as session:
                presence = session.get(Presences, presence_id)
                for key, value in data.items():
                    if (hasattr(presence, key)):
                        setattr(presence, key, value)

                session.commit()
                return presence.to_json()
        except SQLAlchemyError as e:
            session.rollback()
            return e

    def delete(self, presence_id):
        try:
            with Session(self.engine) as session:
                presence = session.get(Presences, presence_id)

                session.delete(presence)
                session.commit()
                return {"Code": "OK"}
        except SQLAlchemyError as e:
            session.rollback()
            return e

    def get_all(self):
        try:
            with Session(self.engine) as session:
                result = session.query(Presences).all()
                presences = [presence.to_json() for presence in result]
                return presences
        except SQLAlchemyError as e:
            return e
