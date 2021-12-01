from fastapi import FastAPI
from configuration.config import TORTOISE_CONFIG
from tortoise.contrib.fastapi import register_tortoise
from endpoints.join import router as join_route
from endpoints.login import router as login_route
from endpoints.api import router as api_route

app = FastAPI()

register_tortoise(app,TORTOISE_CONFIG)

app.add_api_route('/login/', login_route)
app.add_api_route('/join/', join_route)
app.add_api_route('/api/', api_route)
