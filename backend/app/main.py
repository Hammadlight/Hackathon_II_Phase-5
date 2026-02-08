# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
import os

from app.database import engine

# ensure all models are registered
import app.models  # noqa

from app.router import tasks, chat

app = FastAPI(title="Hackathon Todo API")

# ✅ CORS — Azure + Local + Vercel
ALLOW_ORIGINS = [
    "http://20.204.202.125",              # Azure Frontend (AKS)
    "https://hackathon-ii-phase-iii-todo-full-st.vercel.app",
]

ALLOW_ORIGIN_REGEX = r"^http://(localhost|127\.0\.0\.1)(:\d+)?$"

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_origin_regex=ALLOW_ORIGIN_REGEX,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.get("/health")
def health():
    return {"status": "ok", "build": "PHASE5-AZURE-CORS-FIX"}

# ROUTERS
app.include_router(tasks.router, prefix="/api")
app.include_router(chat.router, prefix="/api")
