ABOUT = {
    "name": "Niilo Pääkkönen",
    "title": "M.Sc. Data Science · Software & Data Engineer",
    "bio": (
        "Master of Data Science with a background in software engineering and data engineering. "
        "I conduct full data science projects end-to-end — from data pipelines and classical ML "
        "to LLM-powered systems and production APIs."
    ),
    "location": "Finland",
    "github": "https://github.com/niilop",
    "linkedin": "https://linkedin.com/in/niilopaak",
    "email": "paakkonenniilo@gmail.com",
    "cv_url": "",
}

PROJECTS = [
    {
        "id": "telia-thesis",
        "title": "B2B Revenue Potential — M.Sc. Thesis",
        "description": (
            "Master's thesis conducted for Telia Finland. Built ML models to predict maximum "
            "B2B telecommunications revenue potential for Finnish companies, enabling data-driven "
            "target marketing. Managed end-to-end in Microsoft Fabric: data collection, "
            "cleaning, feature engineering, and model training."
        ),
        "tech": ["Python", "Scikit-learn", "Microsoft Fabric", "Azure", "ML", "Regression"],
        "github": "",
        "demo": "",
        "featured": True,
    },
    {
        "id": "stock-news",
        "title": "Stock News Intelligence",
        "description": (
            "Real-time financial news aggregator with NLP-powered sentiment analysis, "
            "named-entity ticker extraction, and a FastAPI backend serving a React dashboard."
        ),
        "tech": ["Python", "FastAPI", "PostgreSQL", "NLP", "Docker"],
        "github": "https://github.com/niilop/stock-news",
        "demo": "",
        "featured": True,
    },
    {
        "id": "ds-platform",
        "title": "DS Platform Template",
        "description": (
            "Production-ready FastAPI template featuring RAG with pgvector, "
            "persistent multi-turn chat, JWT auth, async background jobs, and "
            "pluggable LLM support (Gemini, OpenAI, Anthropic)."
        ),
        "tech": ["FastAPI", "LangChain", "pgvector", "PostgreSQL", "Docker"],
        "github": "https://github.com/niilop/my-portfolio",
        "demo": "",
        "featured": False,
    },
    {
        "id": "portfolio",
        "title": "This Portfolio",
        "description": (
            "Portfolio site built with FastAPI and Jinja2 — serves both the HTML frontend "
            "and a public REST API. Deployed on Render via Docker with GitHub Actions CI/CD."
        ),
        "tech": ["FastAPI", "Jinja2", "Docker", "GitHub Actions", "Render"],
        "github": "https://github.com/niilop/my-portfolio",
        "demo": "",
        "featured": False,
    },
]

SKILLS = {
    "Languages": ["Python", "SQL", "C++", "Bash"],
    "ML & AI": ["Scikit-learn", "TensorFlow", "LangChain", "Pandas", "NumPy", "Random Forest", "SVM", "Regression", "Deep Learning", "Target Marketing"],
    "Backend & Data": ["FastAPI", "PostgreSQL", "SQLAlchemy", "Alembic", "pgvector", "Kafka", "Docker"],
    "Cloud & Platforms": ["Azure", "Microsoft Fabric", "Snowflake", "Databricks", "Git", "Jira"],
}
