from fastapi import FastAPI
from configuration.config import tortoise_config
from tortoise.contrib.fastapi import register_tortoise
from fastapi_admin.app import app as admin_app
import aioredis


app = FastAPI()

@app.get('/')
async def route():
    return {'It':'Works'}





