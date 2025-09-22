from pydantic import BaseModel, Field

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
    skill               : str
    experience          : str
    qualification       : str
    state               : str
    city                : str
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
    skill               : str = Field(...,example="Skill")
    experience          : str = Field(...,example="Experience")
    qualification       : str = Field(...,example="Qualification")
    state               : str = Field(...,example="State")
    city                : str = Field(...,example="City")
class EmployeesUpdate(BaseModel):
    employees_id        : str = Field(..., example="Enter your emp code")
    first_name          : str = Field(..., example="Potine")
    last_name           : str = Field(..., example="Sambo")
    email               : str = Field(..., example="Sambo")
    phone               : str = Field(..., example="Sambo")
    gender              : str = Field(..., example="M")
    designation         : str = Field(..., example="Designation")
    role                : str = Field(..., example="Trainer")
    skill               : str = Field(...,example="Skill")
    experience          : str = Field(...,example="Experience")
    qualification       : str = Field(...,example="Qualification")
    state               : str = Field(...,example="State")
    city                : str = Field(...,example="City")
    status              : str = Field(..., example="1")
class EmployeesDelete(BaseModel):
    employees_id: str = Field(..., example="Enter your emp code")