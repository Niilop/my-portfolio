from pathlib import Path

from api.endpoints.portfolio import router as portfolio_router
from core.config import get_settings
from core.rate_limit import limiter
from data.portfolio_data import ABOUT, PROJECTS, SKILLS
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

BASE_DIR = Path(__file__).parent

settings = get_settings()

app = FastAPI(
    title="Niilo Paakkonen — Portfolio API",
    description="Public API powering my portfolio site.",
    version="1.0.0",
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

app.include_router(portfolio_router)


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"about": ABOUT, "projects": PROJECTS, "skills": SKILLS},
    )


@app.get("/health")
def health():
    return {"status": "ok"}
