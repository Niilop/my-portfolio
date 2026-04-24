# Niilo Pääkkönen — Portfolio

Personal portfolio site built with FastAPI and Jinja2. Serves both the HTML frontend and a public REST API from a single Docker container, deployed on Render with GitHub Actions CI/CD.

---

## Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI + Uvicorn |
| Frontend | Jinja2 templates + vanilla CSS/JS |
| Tests | pytest + FastAPI TestClient |
| Container | Docker |
| CI/CD | GitHub Actions |
| Hosting | Render (free tier) |

---

## Project Structure

```
my-portfolio/
├── backend/
│   ├── api/endpoints/
│   │   └── portfolio.py      # All API routes
│   ├── core/
│   │   ├── config.py         # Settings (pydantic-settings)
│   │   └── rate_limit.py     # slowapi limiter
│   ├── data/
│   │   └── portfolio_data.py # Content source of truth
│   ├── models/
│   │   └── schemas.py        # Pydantic response models
│   ├── static/
│   │   ├── css/style.css
│   │   └── js/main.js
│   ├── templates/
│   │   ├── base.html
│   │   └── index.html
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── tests/
│   └── test_portfolio.py
├── .github/workflows/ci.yml
├── render.yaml
├── pyproject.toml
└── docker-compose.yaml
```

---

## API Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/` | Portfolio page (HTML) |
| GET | `/health` | Health check |
| GET | `/api/projects` | List all projects |
| GET | `/api/projects/{id}` | Single project |
| GET | `/api/skills` | Skills by category |
| GET | `/api/about` | About info |
| POST | `/api/contact` | Contact form (rate limited 3/min) |
| GET | `/docs` | Swagger UI |

---

## Running Locally

**Option 1 — Direct**

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

**Option 2 — Docker Compose**

```bash
docker compose up --build
```

Open `http://localhost:8000`. No `.env` required to run locally.

---

## Updating Content

All portfolio content lives in one file — no database, no CMS:

```
backend/data/portfolio_data.py
```

Edit `ABOUT`, `PROJECTS`, or `SKILLS` and the changes are reflected on both the HTML page and the API responses.

**Adding a project image:** drop an image into `backend/static/img/` and replace the placeholder div in `index.html`:

```html
<div class="project-card__image">
  <img src="/static/img/your-project.png" alt="Project name" />
</div>
```

---

## Tests

```bash
pytest tests/ -v
```

Tests run in-process via `TestClient` — no live server or database needed.

---

## CI/CD

On every push to `main`:

1. GitHub Actions installs dependencies, runs `ruff` linting and `pytest`
2. If tests pass, a deploy hook triggers Render to redeploy

To set up: copy the deploy hook URL from **Render → Service → Settings → Deploy Hook** and add it as a GitHub repository secret named `RENDER_DEPLOY_HOOK_URL`.

---

## Deployment (Render)

The `render.yaml` at the repo root configures the service. Connect the GitHub repo on [render.com](https://render.com) and it auto-detects the config.

Key settings:

```yaml
runtime: docker
dockerfilePath: ./backend/Dockerfile
dockerContext: .
healthCheckPath: /health
region: frankfurt
```

The free tier spins down after 15 minutes of inactivity — the first request after sleep takes ~30 seconds.

---

## Optional: Contact Form Email Delivery

By default, contact form submissions are logged to stdout (visible in Render's log viewer). To enable email delivery, add these environment variables in the Render dashboard:

```
SMTP_USER=your-gmail@gmail.com
SMTP_PASSWORD=your-app-password
CONTACT_TO_EMAIL=your@email.com
```
