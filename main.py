from fastapi import FastAPI
from routers import services
import models
from databases import engine




app = FastAPI()

@app.get("/healthy")
async def health_check():
    return {"health": "Good"}

# This creates the physical table in .db file
models.Base.metadata.create_all(bind=engine)

app.include_router(services.router)