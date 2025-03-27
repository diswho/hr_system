from datetime import date
from pydantic import BaseModel
from typing import Optional

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: Optional[str] = None
    hire_date: Optional[date] = None
    job_title: Optional[str] = None
    department: Optional[str] = None
    salary: Optional[float] = None
    manager_id: Optional[int] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeInDB(EmployeeBase):
    id: int

    class Config:
        from_attributes = True