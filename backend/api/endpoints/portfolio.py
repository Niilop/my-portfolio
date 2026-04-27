import logging
import smtplib
from email.mime.text import MIMEText

from core.config import get_settings
from core.rate_limit import limiter
from data.portfolio_data import ABOUT, PROJECTS, SKILLS
from fastapi import APIRouter, HTTPException, Request
from models.schemas import AboutOut, ContactIn, ContactOut, ProjectOut, SkillsOut

router = APIRouter(prefix="/api", tags=["Portfolio API"])
logger = logging.getLogger(__name__)


def _send_contact_email(name: str, email: str, message: str) -> None:
    s = get_settings()
    if not s.smtp_user or not s.smtp_password or not s.contact_to_email:
        logger.warning("SMTP not configured — contact form submission dropped")
        return

    body = f"From: {name} <{email}>\n\n{message}"
    msg = MIMEText(body)
    msg["Subject"] = f"Portfolio contact from {name}"
    msg["From"] = s.smtp_user
    msg["To"] = s.contact_to_email

    with smtplib.SMTP(s.smtp_host, s.smtp_port) as server:
        server.starttls()
        server.login(s.smtp_user, s.smtp_password)
        server.sendmail(s.smtp_user, s.contact_to_email, msg.as_string())


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
    try:
        _send_contact_email(body.name, body.email, body.message)
    except Exception:
        logger.exception("Failed to send contact email")
        raise HTTPException(status_code=500, detail="Failed to send message. Please try again later.")
    return ContactOut(success=True, message="Thanks! I'll be in touch soon.")
