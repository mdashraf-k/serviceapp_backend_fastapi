from fastapi import FastAPI
from routers import services
import models
from databases import engine
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           # Allows EVERY website to access your API
    allow_credentials=True,        # Note: Browsers may block if this is True with origins=["*"]
    allow_methods=["*"],           # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],           # Allows all custom headers
)


@app.get("/healthy")
async def health_check():
    return {"health": "Good"}

# This creates the physical table in .db file
models.Base.metadata.create_all(bind=engine)

app.include_router(services.router)