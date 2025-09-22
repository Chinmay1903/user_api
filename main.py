from schema.users import UserList,UserUpdate
from schema.employees import EmployeesList,EmployeesUpdate
from curd.users import UserCurdOperation
from curd.employees import EmployeesCurdOperation
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from typing import List
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from pg_db import database
 
app = FastAPI()

##--------------------------------##
ALLOWED_ORIGINS = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://127.0.0.1:8000",
    "http://localhost:3000",      # React dev server
    "http://127.0.0.1:3000",
    # add your deployed frontend origin(s) here when ready
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,                   # keep False if you don't use cookies
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"], # allow all HTTP methods
    allow_headers=["*"],                        # add others if you send them
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

# Get all users
@app.get("/users", response_model=List[UserList], tags=["Users"])
async def find_all_users():
    return await UserCurdOperation.find_all_users()

# Register user
@app.post("/users", response_model=UserList, tags=["Users"])
async def register_user(user: UserList):
    return await UserCurdOperation.register_user(user)

# Get user by ID
@app.get("/users/{userId}", response_model=UserList, tags=["Users"])
async def find_user_by_id(userId: str):
    user= await UserCurdOperation.find_user_by_id(userId)
    return dict(user)

# Update user
@app.put("/users/{userId}", response_model=UserList, tags=["Users"])
async def update_user(userId: str, user: UserList):
    user.id = userId  # assign path param to body
    return await UserCurdOperation.update_user(user)

# Delete user
@app.delete("/users/{userId}", tags=["Users"])
async def delete_user(userId: str):
    return await UserCurdOperation.delete_user(userId)

# Login
@app.post("/login", tags=["Users"])
async def login(user: UserList):
    return await UserCurdOperation.login(user)

## ---------------- EMPLOYEE ENDPOINTS ----------------

# Get all employees
@app.get("/employees", response_model=List[EmployeesList], tags=["Employees"])
async def find_all_employees():
    return await EmployeesCurdOperation.find_all_employees()

# Register employee
@app.post("/employees", response_model=EmployeesList, tags=["Employees"])
async def register_employee(employee: EmployeesList):
    return await EmployeesCurdOperation.register_employee(employee)

# Get employee by ID
@app.get("/employees/{employeeId}", response_model=EmployeesList, tags=["Employees"])
async def find_employee_by_id(employeeId: str):
    return await EmployeesCurdOperation.find_employees_by_id(employeeId)

# Update employee
# Update employee
@app.put("/employees/{employeeId}", response_model=EmployeesList, tags=["Employees"])
async def update_employee(employeeId: str, employee: EmployeesUpdate):
    employee.employees_id = employeeId  # assign path param into request body
    return await EmployeesCurdOperation.update_employees(employee)

# Delete employee
@app.delete("/employees/{employeeId}", tags=["Employees"])
async def delete_employee(employeeId: str):
    return await EmployeesCurdOperation.delete_employee(employeeId)