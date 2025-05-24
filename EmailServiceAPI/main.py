from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from EmailServiceAPI import models
from EmailServiceAPI.database import engine
from .Routers import user, email

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


@app.get("/", status_code=status.HTTP_200_OK)
def home():
    return JSONResponse(content="hello", status_code=200)


app.include_router(user.router)
app.include_router(email.router)
