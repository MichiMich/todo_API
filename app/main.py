from fastapi import FastAPI

from app.api.api_v1.api import router as api_router

# for wrapping the application in a WSGI server
from mangum import Mangum

app = FastAPI()


@app.get("/")
def read_root():
    return {"Greetings": "Welcome to the todo API"}

app.include_router(api_router, prefix="/v1")


# wrap app in mangum, to enable working with lambda 
handler = Mangum(app)

