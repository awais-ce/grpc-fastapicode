from pydantic import BaseModel , EmailStr
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CreateEmploye(BaseModel):
    firstname : str
    lastname : str
    fathername : str
    cnic : str
    phone : str
    age : int
    address : str
    city : str
    email : str
    join_date : datetime
    

