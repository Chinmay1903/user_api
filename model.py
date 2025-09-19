from pydantic import BaseModel, Field

## Models for User Table
class UserList(BaseModel):
    id        : str
    username  : str
    password  : str
    first_name: str
    last_name : str
    gender    : str
    create_at : str
    status    : str
class UserEntry(BaseModel):
    username  : str = Field(..., example="potinejj")
    password  : str = Field(..., example="potinejj")
    first_name: str = Field(..., example="Potine")
    last_name : str = Field(..., example="Sambo")
    gender    : str = Field(..., example="M")
class UserUpdate(BaseModel):
    id        : str = Field(..., example="Enter your id")
    first_name: str = Field(..., example="Potine")
    last_name : str = Field(..., example="Sambo")
    gender    : str = Field(..., example="M")
    status    : str = Field(..., example="1")
class UserDelete(BaseModel):
    id: str = Field(..., example="Enter your id")

class UserLogin(BaseModel):
    username  : str
    password  : str


## Model for Employees Table
class EmployeesList(BaseModel):
    employees_id        : str
    first_name          : str
    last_name           : str
    email               : str
    phone               : str
    gender              : str
    designation         : str
    role                : str
    create_at           : str
    status              : str
class EmployeesEntry(BaseModel):
    employees_id        : str = Field(..., example="potinejj")
    first_name          : str = Field(..., example="Potine")
    last_name           : str = Field(..., example="Sambo")
    email               : str = Field(..., example="Sambo")
    phone               : str = Field(..., example="Sambo")
    gender              : str = Field(..., example="M")
    designation         : str = Field(..., example="Designation")
    role                : str = Field(...,example="Trainer")
class EmployeesUpdate(BaseModel):
    employees_id        : str = Field(..., example="Enter your emp code")
    first_name          : str = Field(..., example="Potine")
    last_name           : str = Field(..., example="Sambo")
    email               : str = Field(..., example="Sambo")
    phone               : str = Field(..., example="Sambo")
    gender              : str = Field(..., example="M")
    designation         : str = Field(..., example="Designation")
    role                : str = Field(..., example="Trainer")
    status              : str = Field(..., example="1")
class EmployeesDelete(BaseModel):
    employees_id: str = Field(..., example="Enter your emp code")