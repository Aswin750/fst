from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,Text,Numeric


Base=declarative_base()
class user(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True, index=True)
    name=Column(String(30),nullable=False)
    email=Column(String(30),nullable=True)
    phone = Column(Numeric(10), nullable=False)
    password_hash = Column(Text, nullable=False)
    role = Column(String(20), nullable=False)
    created_at = Column(DateTime, nullable=True)

class student(Base):
    __tablename__="students"
    student_identifier=Column(String,primary_key=True, index=True)
    student_id=Column(Integer)
    class_name=Column(String)