import datetime, uuid
from schema.roles import RolesDelete,RolesEntry,RolesUpdate
from pg_db import database,roles


## End Point for Roles Table

class RolesCurdOperation:

    ## All roles
    @staticmethod
    async def find_all_roles():
        query = roles.select()
        return await database.fetch_all(query)
    
    ## Roles register
    @staticmethod
    async def register_role(role: RolesEntry):
        gDate =str(datetime.datetime.now())
        query = roles.insert().values(
            role_id    =    str(uuid.uuid4()),
            role_name  =     role.role_name,
            create_at  =     gDate
        )
        await database.execute(query)
        return {**role.dict(), "create_at": gDate}  
    
    ## Update roles
    @staticmethod
    async def update_role(role: RolesUpdate):
        query = roles.update().where(roles.c.role_id == role.role_id).values(
            role_name=role.role_name
        )
        await database.execute(query)
        return {**role.dict()}
    
    ## Delete roles
    @staticmethod
    async def delete_role(role: RolesDelete):
        query = roles.delete().where(roles.c.role_id == role.role_id)
        await database.execute(query)
        return {"message": "Role deleted successfully"}
