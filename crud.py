from fastapi import FastAPI , Depends , HTTPException
from models import Employee
from sqlalchemy.orm import Session
from schemas import *


def create_employee(db  : Session , employee = CreateEmploye):
    db_employee = Employee(firstname = employee.firstname , lastname = employee.lastname , 
                         fathername = employee.fathername , cnic = employee.cnic , phone = employee.phone , 
                         age = employee.age , address = employee.address , city = employee.city , 
                         email = employee.email  , join_date = employee.join_date)
    
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def get_employee(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()

def update_employee(employee_id: int, db: Session, employee: CreateEmploye):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if db_employee is None:
        return None

    db_employee.firstname = employee.firstname
    db_employee.lastname = employee.lastname
    db_employee.fathername = employee.fathername
    db_employee.cnic = employee.cnic
    db_employee.phone = employee.phone
    db_employee.age = employee.age
    db_employee.address = employee.address
    db_employee.city = employee.city
    db_employee.email = employee.email
    db_employee.join_date = employee.join_date

    db.commit()
    db.refresh(db_employee)

    return db_employee


def delete_employee(employee_id : int , db : Session):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if delete_employee is None:
        raise HTTPException(status_code=404 , detail="Employe Data Successfuly Delete")
    
    db.delete(db_employee)
    db.commit()
    db.refresh(db_employee)
    return {"detail": "Employee Data Successfully Deleted"}
    



