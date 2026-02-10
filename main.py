from fastapi import FastAPI

from auth_routes import auth_route
from order_routes import order_route

app = FastAPI()

app.include_router(auth_route)
app.include_router(order_route)
