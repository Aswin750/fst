from pydantic import BaseModel,EmailStr,Field,ConfigDict
from datetime import datetime

class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=30)
    email: EmailStr
    phone: str = Field(pattern=r"^\d{10}$")
    password: str = Field(min_length=8)
    role: str = Field(min_length=1, max_length=20)





