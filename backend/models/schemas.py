from pydantic import BaseModel, EmailStr


class ProjectOut(BaseModel):
    id: str
    title: str
    description: str
    tech: list[str]
    github: str
    demo: str
    featured: bool


class SkillsOut(BaseModel):
    categories: dict[str, list[str]]


class AboutOut(BaseModel):
    name: str
    title: str
    bio: str
    location: str
    github: str
    linkedin: str
    email: str
    cv_url: str


class ContactIn(BaseModel):
    name: str
    email: EmailStr
    message: str


class ContactOut(BaseModel):
    success: bool
    message: str
