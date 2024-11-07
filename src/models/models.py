from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine

from enums.enums import RoleEnum

Base = declarative_base()
engine = create_engine("postgresql://postgres:123456789@localhost:5432/inar")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False, default=RoleEnum.user)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "role": self.role.get_value(),
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get("id"),
            username=data.get("username"),
            password=data.get("password"),
            role=data.get("role")
        )

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    employees = relationship("Employee", back_populates="department", cascade="all, delete", passive_deletes=True)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get("id"),
            name=data.get("name")
        )


class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    department_id = Column(Integer, ForeignKey("departments.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    department = relationship("Department", back_populates="employees")
    presences = relationship("Presences", back_populates="employee", cascade="all, delete", passive_deletes=True)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "department_id": self.department_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            surname=data.get("surname"),
            email=data.get("email"),
            department_id=data.get("department_id")
        )

class Presences(Base):
    __tablename__ = "presences"
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), nullable=False)
    date = Column(String, nullable=True)
    presences = Column(Integer, nullable=False)
    absences = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    employee = relationship("Employee", back_populates="presences")

    def to_json(self):
        return {
            "id": self.id,
            "employee_id": self.employee_id,
            "date": self.date,
            "presences": self.presences,
            "absences": self.absences,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get("id"),
            employee_id=data.get("employee_id"),
            date=data.get("date"),
            presences=data.get("presences"),
            absences=data.get("absences")
        )


def get_storage():
    Base.metadata.create_all(engine)