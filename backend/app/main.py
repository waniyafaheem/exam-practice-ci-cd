from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from .database import init_db
from .routers.todos import router as todos_router

app = FastAPI()

frontend_url = os.getenv("FRONTEND_URL", "*")
print("Allowing CORS from:", frontend_url)  # Helpful for debugging

# Don't allow "*" if you plan to use cookies or Authorization headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup():
    await init_db()

app.include_router(todos_router)