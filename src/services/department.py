from sqlalchemy.orm import Session
from models.models import Department
from sqlalchemy.exc import SQLAlchemyError
from services.service import Service

class DepartmentService(Service):
    def __init__(self, engine):
        super().__init__(engine)

    def create(self, data):
        try:
            with Session(self.engine) as session:
                new_department = Department(
                    name=data.get('name')
                )
                session.add(new_department)
                session.commit()
                return new_department.to_json()
        except SQLAlchemyError as e:
            session.rollback()
            return e

    def update(self, department_id, data):
        try:
            with Session(self.engine) as session:
                department = session.get(Department, department_id)
                for key, value in data.items():
                    if (hasattr(department, key)):
                        setattr(department, key, value)        
                session.commit()
                return department.to_json()
        except SQLAlchemyError as e:
            session.rollback()
            return e

    def delete(self, department_id):
        try:
            with Session(self.engine) as session:
                department = session.get(Department, department_id)
                
                session.delete(department)
                session.commit()
                return {"Code": "OK"}
        except SQLAlchemyError as e:
            session.rollback()
            return e

    def get_all(self):
        try:
            with Session(self.engine) as session:
                departments = session.query(Department).all()
                return departments
        except SQLAlchemyError as e:
            return e 