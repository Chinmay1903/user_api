import datetime, uuid
import model as mdUser
from pg_db import database, users,employees
from fastapi import FastAPI,HTTPException,Depends 
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from passlib.context import CryptContext
from contextlib import asynccontextmanager ##new
from fastapi.middleware.cors import CORSMiddleware
 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI()

##--------------------------------##
ALLOWED_ORIGINS = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    # add your deployed frontend origin(s) here when ready
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,                   # keep False if you don't use cookies
    allow_methods=["POST", "OPTIONS"],         # include OPTIONS for preflight
    allow_headers=["Content-Type","Authorization"],            # add others if you send them
)
##---------------------------------##

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    print("🚀 App starting...")
    yield
    # Shutdown logic
    print("🛑 App shutting down...")

# ✅ Connect on startup
@app.on_event("startup")
async def startup():
    await database.connect()

# ✅ Disconnect on shutdown
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

## End Point for User table.

@app.get("/users", response_model=List[mdUser.UserList], tags=["Users"])
async def find_all_users():
    query = users.select()
    return await database.fetch_all(query)

@app.post("/users", response_model=mdUser.UserList, tags=["Users"])
async def register_user(user: mdUser.UserEntry):
    gID   = str(uuid.uuid1())
    gDate =str(datetime.datetime.now())
    query = users.insert().values(
        id = gID,
        username   = user.username,
        password   = pwd_context.hash(user.password),
        first_name = user.first_name,
        last_name  = user.last_name,
        gender     = user.gender,
        create_at  = gDate,
        status     = "1"
    ) 

    await database.execute(query)
    return {
        "id": gID,
        **user.dict(),
        "create_at":gDate,
        "status": "1"
    }

@app.get("/users/{userId}", response_model=mdUser.UserList, tags=["Users"])
async def find_user_by_id(userId: str):
    query = users.select().where(users.c.id == userId)
    return await database.fetch_one(query)

@app.put("/users", response_model=mdUser.UserList, tags=["Users"])
async def update_user(user: mdUser.UserUpdate):
    gDate = str(datetime.datetime.now())
    query = users.update().\
        where(users.c.id == user.id).\
        values(
            first_name = user.first_name,
            last_name  = user.last_name,
            gender     = user.gender,
            status     = user.status,
            create_at  = gDate,
        )
    await database.execute(query)

    return await find_user_by_id(user.id)

@app.delete("/users/{userId}", tags=["Users"])
async def delete_user(user: mdUser.UserDelete):
    query = users.delete().where(users.c.id == user.id)
    await database.execute(query)

    return {
        "status" : True,
        "message": "This user has been deleted successfully." 
    }

###---------------------------------LOGIN-------------------------------------####
@app.post("/login", tags=["Users"])
async def login(user: mdUser.UserLogin):
    query = users.select().where(users.c.username == user.username)
    db_user = await database.fetch_one(query)

    if not db_user or not pwd_context.verify(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    return {"status": True,"message": "Login successful"}

###---------------------------------------------------------------------------####


## End Point for Employees Table
@app.get("/employees", response_model=List[mdUser.EmployeesList], tags=["Employees"])
async def find_all_employees():
    query = employees.select()
    return await database.fetch_all(query)

@app.post("/employees", response_model=mdUser.EmployeesList, tags=["Employees"])
async def register_employee(employee: mdUser.EmployeesEntry):
    gDate =str(datetime.datetime.now())
    query = employees.insert().values(
        employees_id   = employee.employees_id,
        first_name =     employee.first_name,
        last_name  =     employee.last_name,
        email      =     employee.email,
        phone      =     employee.phone,
        gender     =     employee.gender,
        designation=     employee.designation,
        role       =     employee.role,
        create_at  =     gDate,
        status     =     "1"
    ) 

    await database.execute(query)
    return {
        **employee.dict(),
        "create_at":gDate,
        "status": "1"
    }

@app.get("/employees/{employees_id}", response_model=mdUser.EmployeesList, tags=["Employees"])
async def find_employees_by_id(employees_id: str):
    query = employees.select().where(employees.c.employees_id == employees_id)
    return await database.fetch_one(query)

@app.put("/employees", response_model=mdUser.EmployeesList, tags=["Employees"])
async def update_employees(employee: mdUser.EmployeesUpdate):
    gDate = str(datetime.datetime.now())
    query = employees.update().\
        where(employees.c.employees_id == employee.employees_id).\
        values(
            first_name =     employee.first_name,
            last_name  =     employee.last_name,
            email      =     employee.email,
            phone      =     employee.phone,
            gender     =     employee.gender,
            designation=     employee.designation,
            role       =     employee.role,
            status     =     employee.status,
            create_at  =     gDate,
        )
    await database.execute(query)

    return await find_employees_by_id(employee.employees_id)

@app.delete("/employees/{employees_Id}", tags=["Employees"])
async def delete_employees(employee: mdUser.EmployeesDelete):
    query = employees.delete().where(employees.c.employees_id == employee.employees_id)
    await database.execute(query)

    return {
        "status" : True,
        "message": "This employees has been deleted successfully." 
    }