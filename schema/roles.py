from pydantic import BaseModel, Field

## Models for Roles Table
class RolesList(BaseModel):
    role_id   : str
    role_name : str
    create_at : str
class RolesEntry(BaseModel):
    role_name : str = Field(..., example="Trainer")
class RolesUpdate(BaseModel):
    role_id   : str = Field(..., example="Enter your role id")
    role_name : str = Field(..., example="Trainer")
class RolesDelete(BaseModel):
    role_id: str = Field(..., example="Enter your role id")