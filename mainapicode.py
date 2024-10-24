from fastapi import FastAPI , Depends , HTTPException
from database import *
from schemas import CreateEmploye
from sqlalchemy.orm import Session
from crud import *
from models import *
import grpc 
import greet_pb2
import greet_pb2_grpc

app = FastAPI()


def get_db():
    db = sessionLocal()
    try:
        yield db
    
    finally:
        db.close()

Base.metadata.create_all(bind = engine)


def grpc_say_hello(name: str) -> str:
    try:
        with grpc.insecure_channel("localhost:50051") as channel:
            stub = greet_pb2_grpc.GreeterStub(channel)
            response = stub.SayHello(greet_pb2.HelloRequest(name=name))
            return response.message
    except grpc.RpcError as e:
        print(f"gRPC error: {e.code()} - {e.details()}")
        return "gRPC call successfully"


@app.post("/employee/create")
async def create_employee_api(employee : CreateEmploye , db : Session = Depends(get_db)):


    grpc_response = grpc_say_hello(employee.firstname)

    # if grpc_response == "Grpc call not faild":
        # raise HTTPException(status_code=404 , detail = "Grpc response are not found")

    db_employee =  create_employee(db ,employee)

    

    return {"grpc_response"  : grpc_response , "employee"  : db_employee}




@app.get("/employee/{employee_id}")
async def get_employee_api(employee_id: int, db: Session = Depends(get_db)):
    db_employee = get_employee(db, employee_id)

    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    grpc_response = grpc_say_hello("Muhammad Awais")
    return {"grpc_response" : grpc_response , "employee" : db_employee}

@app.post("/employee/update/{employee_id}")
async def update_employee_api(employee: CreateEmploye, employee_id: int, db: Session = Depends(get_db)):
    db_employee = update_employee(employee_id, db, employee)  
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    grpc_response = grpc_say_hello(employee.firstname)
    return {"grpc_response" : grpc_response, "employee" :db_employee}

@app.post("/employee/delete/{employee_id}")
async def delete_employee_api(employee_id: int, db: Session = Depends(get_db)):
    db_employee = delete_employee(employee_id, db)

    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee Data Not Found")
    
    # Call the gRPC service
    grpc_response = grpc_say_hello("Muhammad Awais")
    
    return {"grpc_response": grpc_response, "employee_deleted": True}
