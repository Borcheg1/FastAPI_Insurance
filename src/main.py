from fastapi import FastAPI
from tortoise import Tortoise

from src.config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME


app = FastAPI()


@app.on_event("startup")
async def db_connection():
    """
    Initial database connect
    """
    try:
        await Tortoise.init(
            db_url=f'postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}',
            modules={'models': ['main']}
        )
        await Tortoise.generate_schemas()
        print("Database connection was successfull")
    except Exception as error:
        print("Connection to database failed")
        print(f"Error: {error}")


@app.on_event('shutdown')
async def shutdown():
    """
    Shutdown database connect
    """
    await Tortoise.close_connections()
