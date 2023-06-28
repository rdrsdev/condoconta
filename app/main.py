import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware
from mangum import Mangum

from app.settings.db import DATABASE_URL, engine
from app.settings.env import PROJECT_NAME, DEBUG, VERSION, API_PREFIX
from app.settings.events import create_start_app_handler, create_stop_app_handler
from app.settings.routes import router as api_router

app = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)

app.add_event_handler(
    "startup", create_start_app_handler(app))
app.add_event_handler(
    "shutdown", create_stop_app_handler(app))

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(DBSessionMiddleware, db_url=DATABASE_URL, custom_engine=engine)
app.include_router(api_router, prefix=API_PREFIX)

handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
