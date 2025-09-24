import datetime, uuid
from schema.employees import EmployeesDelete,EmployeesEntry,EmployeesUpdate
from pg_db import database,employees
from passlib.context import CryptContext
 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


## End Point for Employees Table

class EmployeesCurdOperation:

    ## All employees
    @staticmethod
    async def find_all_employees():
        query = employees.select()
        return await database.fetch_all(query)
    
    ## All employees with ID and Name
    @staticmethod
    async def find_all_employees_name():
        query = employees.select().with_only_columns(
            employees.c.employees_id, 
            employees.c.first_name, 
            employees.c.last_name
        )
        result = await database.fetch_all(query)
        return [
            {
                "employees_id": row["employees_id"],
                "full_name": f"{row['first_name']} {row['last_name']}"
            }
            for row in result
        ]
    
    ## All Managers with ID and Name
    @staticmethod
    async def all_managers_name():
        query = employees.select().where(employees.c.role == 'Manager').with_only_columns(
            employees.c.employees_id, 
            employees.c.first_name, 
            employees.c.last_name
        )
        result = await database.fetch_all(query)
        return [
            {
                "employees_id": row["employees_id"],
                "full_name": f"{row['first_name']} {row['last_name']}"
            }
            for row in result
        ]

    ## Employees register
    @staticmethod
    async def register_employee(employee: EmployeesEntry):
        gDate =str(datetime.datetime.now())
        query = employees.insert().values(
            employees_id   =    employee.employees_id,
            first_name     =     employee.first_name,
            last_name      =     employee.last_name,
            email          =     employee.email,
            phone          =     employee.phone,
            gender         =     employee.gender,
            designation    =     employee.designation,
            role           =     employee.role,
            skill          =     employee.skill,        
            experience     =     employee.experience,         
            qualification  =     employee.qualification,     
            state          =     employee.state, 
            city           =     employee.city,
            create_at      =     gDate,
            status         =     "1"
        ) 

        await database.execute(query)
        return {
            **employee.dict(),
            "create_at":gDate,
            "status": "1"
        }
    ## Find Employees by ID
    @staticmethod
    async def find_employees_by_id(employees_id: str):
        query = employees.select().where(employees.c.employees_id == employees_id)
        return await database.fetch_one(query)

    ## Employees update
    @staticmethod
    async def update_employees(employee: EmployeesUpdate):
        gDate = str(datetime.datetime.now())
        query = employees.update().\
            where(employees.c.employees_id == employee.employees_id).\
            values(
                first_name     = employee.first_name,
                last_name      = employee.last_name,
                email          = employee.email,
                phone          = employee.phone,
                gender         = employee.gender,
                designation    = employee.designation,
                role           = employee.role,
                skill          = employee.skill,        
                experience     = employee.experience,         
                qualification  = employee.qualification,     
                state          = employee.state, 
                city           = employee.city,
                status         = employee.status,
                create_at      = gDate,
            )
        await database.execute(query)

        # ✅ Fetch and return updated employee
        return await EmployeesCurdOperation.find_employees_by_id(employee.employees_id)


    ## Employees Delete
## Employees Delete
    @staticmethod
    async def delete_employee(employeeId: str):
        # 1. Check if employee exists
        existing = await EmployeesCurdOperation.find_employees_by_id(employeeId)
        if not existing:
            return {"status": False, "message": "Employee not found."}

        # 2. If exists, delete
        query = employees.delete().where(employees.c.employees_id == employeeId)
        await database.execute(query)

        return {"status": True, "message": "Employee has been deleted successfully."}