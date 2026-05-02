import re
from pathlib import Path

import markdown
from api.endpoints.portfolio import router as portfolio_router
from core.config import get_settings
from core.rate_limit import limiter
from data.portfolio_data import ABOUT, PROJECTS, SKILLS
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

BASE_DIR = Path(__file__).parent
BLOG_DIR = BASE_DIR / "data" / "blog"


def _parse_frontmatter(text: str) -> tuple[dict, str]:
    match = re.match(r"^---\n(.*?)\n---\n?", text, re.DOTALL)
    if not match:
        return {}, text
    meta: dict = {}
    for line in match.group(1).splitlines():
        if ": " in line:
            k, v = line.split(": ", 1)
            meta[k.strip()] = v.strip().strip('"')
    return meta, text[match.end():]

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


def _first_paragraph(body: str) -> str:
    for line in body.splitlines():
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith("<"):
            return re.sub(r"\*{1,2}|`", "", line)
    return ""


@app.get("/blog", response_class=HTMLResponse)
def blog_index(request: Request):
    posts = []
    if BLOG_DIR.exists():
        for f in BLOG_DIR.glob("*.md"):
            meta, body = _parse_frontmatter(f.read_text(encoding="utf-8"))
            posts.append({
                "slug": f.stem,
                "title": meta.get("title", f.stem),
                "date": meta.get("date", ""),
                "summary": meta.get("summary", ""),
                "github": meta.get("github", ""),
                "preview": _first_paragraph(body),
            })
        posts.sort(key=lambda p: p["date"], reverse=True)
    return templates.TemplateResponse(
        request=request,
        name="blog_index.html",
        context={"about": ABOUT, "posts": posts},
    )


@app.get("/blog/{slug}", response_class=HTMLResponse)
def blog_post(request: Request, slug: str):
    path = BLOG_DIR / f"{slug}.md"
    if not path.exists():
        raise HTTPException(status_code=404, detail="Post not found")
    meta, body = _parse_frontmatter(path.read_text(encoding="utf-8"))
    md = markdown.Markdown(extensions=["tables", "fenced_code", "extra", "toc"], extension_configs={"toc": {"toc_depth": "2"}})
    html_content = md.convert(body)
    return templates.TemplateResponse(
        request=request,
        name="blog_post.html",
        context={"about": ABOUT, "meta": meta, "content": html_content, "toc": md.toc},
    )


@app.get("/health")
def health():
    return {"status": "ok"}
