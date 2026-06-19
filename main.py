from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import init_db
from app.routers import auth, projects, sessions, analytics

app = FastAPI(
    title="Claude Code Session Tracker",
    description="Track and analyze your Claude Code sessions, costs, and model performance",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(projects.router)
app.include_router(sessions.router)
app.include_router(analytics.router)


@app.on_event("startup")
def startup():
    init_db()


@app.get("/", tags=["Health"])
def root():
    return {
        "name": "Claude Code Session Tracker",
        "version": "1.0.0",
        "docs": "/docs",
        "status": "running"
    }


@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}
