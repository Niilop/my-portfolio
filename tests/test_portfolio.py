from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestHealth:
    def test_health_returns_ok(self):
        r = client.get("/health")
        assert r.status_code == 200
        assert r.json() == {"status": "ok"}


class TestPortfolioPage:
    def test_root_returns_html(self):
        r = client.get("/")
        assert r.status_code == 200
        assert "text/html" in r.headers["content-type"]

    def test_root_contains_name(self):
        r = client.get("/")
        assert "Niilo" in r.text

    def test_root_contains_all_sections(self):
        r = client.get("/")
        for section_id in ["about", "projects", "skills", "contact"]:
            assert f'id="{section_id}"' in r.text


class TestProjectsAPI:
    def test_get_projects_returns_list(self):
        r = client.get("/api/projects")
        assert r.status_code == 200
        data = r.json()
        assert isinstance(data, list)
        assert len(data) > 0

    def test_project_schema(self):
        r = client.get("/api/projects")
        project = r.json()[0]
        for field in ["id", "title", "description", "tech", "github", "demo", "featured"]:
            assert field in project

    def test_get_project_by_id(self):
        projects = client.get("/api/projects").json()
        project_id = projects[0]["id"]
        r = client.get(f"/api/projects/{project_id}")
        assert r.status_code == 200
        assert r.json()["id"] == project_id

    def test_get_project_not_found(self):
        r = client.get("/api/projects/does-not-exist")
        assert r.status_code == 404


class TestSkillsAPI:
    def test_get_skills_returns_categories(self):
        r = client.get("/api/skills")
        assert r.status_code == 200
        data = r.json()
        assert "categories" in data
        assert isinstance(data["categories"], dict)

    def test_skills_have_expected_categories(self):
        r = client.get("/api/skills")
        cats = r.json()["categories"]
        for expected in ["Languages", "ML & AI", "Backend & Data", "Cloud & Platforms"]:
            assert expected in cats


class TestAboutAPI:
    def test_get_about_returns_200(self):
        r = client.get("/api/about")
        assert r.status_code == 200

    def test_about_schema(self):
        r = client.get("/api/about")
        data = r.json()
        for field in ["name", "title", "bio", "location", "github", "linkedin", "email", "cv_url"]:
            assert field in data


class TestContactAPI:
    def test_contact_success(self):
        r = client.post("/api/contact", json={
            "name": "Test User",
            "email": "test@example.com",
            "message": "Hello from tests",
        })
        assert r.status_code == 200
        data = r.json()
        assert data["success"] is True
        assert "message" in data

    def test_contact_invalid_email(self):
        r = client.post("/api/contact", json={
            "name": "Test",
            "email": "not-an-email",
            "message": "Hello",
        })
        assert r.status_code == 422

    def test_contact_missing_fields(self):
        r = client.post("/api/contact", json={"name": "Test"})
        assert r.status_code == 422
