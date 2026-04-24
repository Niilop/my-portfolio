import logging

from core.rate_limit import limiter
from data.portfolio_data import ABOUT, PROJECTS, SKILLS
from fastapi import APIRouter, HTTPException, Request
from models.schemas import AboutOut, ContactIn, ContactOut, ProjectOut, SkillsOut

router = APIRouter(prefix="/api", tags=["Portfolio API"])
logger = logging.getLogger(__name__)


@router.get("/projects", response_model=list[ProjectOut])
def get_projects():
    return PROJECTS


@router.get("/projects/{project_id}", response_model=ProjectOut)
def get_project(project_id: str):
    for p in PROJECTS:
        if p["id"] == project_id:
            return p
    raise HTTPException(status_code=404, detail="Project not found")


@router.get("/skills", response_model=SkillsOut)
def get_skills():
    return {"categories": SKILLS}


@router.get("/about", response_model=AboutOut)
def get_about():
    return ABOUT


@router.post("/contact", response_model=ContactOut)
@limiter.limit("3/minute")
def post_contact(request: Request, body: ContactIn):
    logger.info("Contact form — name=%s email=%s", body.name, body.email)
    return ContactOut(success=True, message="Thanks! I'll be in touch soon.")
