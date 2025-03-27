from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..session import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String)
    hire_date = Column(Date)
    job_title = Column(String)
    department = Column(String)
    salary = Column(Float)
    manager_id = Column(Integer, ForeignKey("employees.id"))
    address = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
    country = Column(String)

    manager = relationship("Employee", remote_side=[id])

    def __repr__(self):
        return f"<Employee {self.first_name} {self.last_name}>"