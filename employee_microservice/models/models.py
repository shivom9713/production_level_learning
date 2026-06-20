from pydantic import BaseModel, EmailStr
from typing import Optional

class Employee(BaseModel):
    id: int
    name: str
    email: EmailStr
    department: str


## Output model for the index route
class Index(BaseModel):
    health: str
    status: str