from fastapi import FastAPI
from app.routes import sensor_route

app = FastAPI(title="H2OControl API")

app.include_router(sensor_route.router)
