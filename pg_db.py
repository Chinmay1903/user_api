import databases, sqlalchemy

## Postgres Database
DATABASE_URL = "postgresql://gms_server_database_user:xAJMcH21ibrri3OpltVTrvqQR04SbtJO@dpg-d38irepr0fns7381pdl0-a.oregon-postgres.render.com/gms_server_database"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

## Create a User Table.
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String, primary_key=True, auto_increment=True),
    sqlalchemy.Column("username"  , sqlalchemy.String),
    sqlalchemy.Column("password"  , sqlalchemy.String),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name" , sqlalchemy.String),
    sqlalchemy.Column("gender"    , sqlalchemy.CHAR  ),
    sqlalchemy.Column("create_at" , sqlalchemy.String),
    sqlalchemy.Column("status"    , sqlalchemy.CHAR  ),
)

## Create a Employees Table.
employees = sqlalchemy.Table(
    "employees",
    metadata,

    sqlalchemy.Column("employees_id"        , sqlalchemy.String, nullable=False, unique=True),
    sqlalchemy.Column("first_name"          , sqlalchemy.String),
    sqlalchemy.Column("last_name"           , sqlalchemy.String),
    sqlalchemy.Column("email"               , sqlalchemy.String),
    sqlalchemy.Column("phone"               , sqlalchemy.String),
    sqlalchemy.Column("gender"              , sqlalchemy.String),
    sqlalchemy.Column("designation"         , sqlalchemy.String),
    sqlalchemy.Column("role"                , sqlalchemy.String, sqlalchemy.ForeignKey("roles.role_id")),
    sqlalchemy.Column("skill"               , sqlalchemy.String),
    sqlalchemy.Column("experience"          , sqlalchemy.String),
    sqlalchemy.Column("qualification"       , sqlalchemy.String),
    sqlalchemy.Column("state"               , sqlalchemy.String),
    sqlalchemy.Column("city"                , sqlalchemy.String),
    sqlalchemy.Column("create_at"           , sqlalchemy.String),
    sqlalchemy.Column("status"              , sqlalchemy.CHAR  ),
)


## Create a Roles Table
roles = sqlalchemy.Table(
    "roles",
    metadata,
    sqlalchemy.Column("role_id",    sqlalchemy.String, primary_key=True, auto_increment=True),
    sqlalchemy.Column("role_name",  sqlalchemy.String, unique=True, nullable=False),
    sqlalchemy.Column("create_at",  sqlalchemy.String),
)



engine = sqlalchemy.create_engine(
    DATABASE_URL
)
metadata.create_all(engine)