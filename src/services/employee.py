from sqlalchemy.orm import Session
from models.models import Employee
from sqlalchemy.exc import SQLAlchemyError
from services.service import Service

class EmployeeService(Service):
    def __init__(self, engine):
        super().__init__(engine)

    def create(self, data):
        try:
            with Session(self.engine) as session:
                new_employee = Employee(
                    name=data.get('name'),
                    surname=data.get('surname'),
                    email=data.get('email'),
                    department_id=data.get('department_id')
                )
                session.add(new_employee)
                session.commit()
                return new_employee.to_json()
        except SQLAlchemyError as e:
            session.rollback()
            return e

    def update(self, employee_id, data):
        try:
            with Session(self.engine) as session:
                employee = session.get(Employee, employee_id)

                for key, value in data.items():
                    if (hasattr(employee, key)):
                        setattr(employee, key, value)                
                session.commit()
                return employee.to_json()
        except SQLAlchemyError as e:
            session.rollback()
            return e

    def delete(self, employee_id):
        try:
            with Session(self.engine) as session:
                employee = session.get(Employee, employee_id)
                session.delete(employee)
                session.commit()
                return {"Code": "OK"}
        except SQLAlchemyError as e:
            session.rollback()
            return e
        
    def get_all(self):
        try:
            with Session(self.engine) as session:
                result = session.query(Employee).all()
                employees = [employee.to_json() for employee in result]
                return employees
        except SQLAlchemyError as e:
            return e