from sqlalchemy import String , Integer , Column , DateTime
from database import Base

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String)
    lastname = Column(String)
    fathername = Column(String)
    cnic = Column(String)
    phone = Column(String)
    age = Column(Integer)
    address = Column(String)
    city = Column(String)
    email = Column(String)
    join_date = Column(DateTime)