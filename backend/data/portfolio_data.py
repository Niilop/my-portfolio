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
        "tech": ["Python", "Scikit-learn", "Microsoft Fabric", "Azure", "Regression"],
        "github": "",
        "demo": "",
        "image": "/static/images/project-thesis.jpg",
        "featured": False,
    },
    {
        "id": "mario-ddqn",
        "title": "Super Mario Land — DDQN Agent",
        "description": (
            "Trained a Double Deep Q-Network (DDQN) reinforcement learning agent to play "
            "Super Mario Land. Covers environment wrappers, replay memory, target network "
            "updates, and reward shaping to achieve stable game-playing behaviour."
        ),
        "tech": ["Python", "PyTorch", "Reinforcement Learning", "DDQN", "OpenAI Gym"],
        "github": "https://github.com/niilop/Super-Mario-Land-DDQN-Project",
        "demo": "",
        "image": "/static/images/MarioAI.gif",
        "image_position": "bottom",
        "featured": True,
        "blog_post": "ddqn-mario-project",
    },
    {
        "id": "stock-sentiment",
        "title": "Stock Sentiment",
        "description": (
            "Collects historical and real-time stock news via the Alpaca API and runs "
            "FinBERT sentiment analysis on each article. Users select a time frame and "
            "get a breakdown of positive, neutral, and negative news for any ticker. "
            "News stored in Azure Blob Storage and cleaned in Databricks using a "
            "medallion architecture."
        ),
        "tech": ["Python", "FinBERT", "Alpaca API", "Azure Blob", "Databricks", "FastAPI"],
        "github": "https://github.com/niilop/stock-sentiment",
        "demo": "",
        "image": "/static/images/project-stock.jpg",
        "featured": False,
    },
    {
        "id": "fastapi-template",
        "title": "My FastAPI Template",
        "description": (
            "Production-ready FastAPI template used as the foundation for most of my "
            "Python software projects. Includes RAG with pgvector, persistent chat, "
            "JWT auth, async background jobs, and pluggable LLM support."
        ),
        "tech": ["FastAPI", "LangChain", "pgvector", "PostgreSQL", "Docker"],
        "github": "https://github.com/niilop/My-FastAPI-template",
        "demo": "",
        "image": "/static/images/project-fastapi.jpg",
        "featured": False,
    },
    {
        "id": "ml-sandbox",
        "title": "ML Sandbox",
        "description": (
            "Platform for uploading and hosting ML models and datasets, with agentic "
            "sentiment analysis on uploaded data. Supports model management, dataset "
            "exploration, and AI-driven insight generation."
        ),
        "tech": ["Python", "FastAPI", "LangChain", "Scikit-learn", "Pandas", "Docker"],
        "github": "https://github.com/niilop/ml-sandbox",
        "demo": "",
        "image": "/static/images/project-ml-sandbox.jpg",
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
        "image": "/static/images/my-portfolio.jpg",
        "featured": False,
    },
    {
        "id": "model-selection-agent",
        "title": "LLM Model Selection Agent",
        "description": (
            "A Claude-powered agent that profiles a regression dataset and reasons about which "
            "model families to try — compared head-to-head against exhaustive GridSearchCV (715 CV fits) "
            "and Optuna Bayesian optimisation (500 CV fits). The agent matched or beat both baselines "
            "using ~30 CV fits per dataset, with its clearest win on Energy Efficiency (−5.9% vs GridSearch)."
        ),
        "tech": ["Python", "Claude API", "Scikit-learn", "Optuna", "Pandas", "Anthropic SDK"],
        "github": "https://github.com/Niilop/model-selection-agent",
        "demo": "",
        "image": "",
        "featured": True,
        "blog_post": "model-selection-agent",
    },
    {
        "id": "warehouse-sim",
        "title": "Warehouse Optimization Simulator",
        "description": (
            "Full-stack warehouse optimization simulator with A* pathfinding, realistic demand modeling, "
            "and data-driven slotting strategies. Includes real-time WebSocket visualization, a browser "
            "layout editor, and a Jupyter analysis pipeline for comparing performance across scenarios."
        ),
        "tech": ["Python","NumPy","FastAPI","WebSockets","AsyncIO","JavaScript","HTML/CSS","Matplotlib",],
        "github": "https://github.com/Niilop/storage-sim",
        "demo": "",
        "image": "/static/images/warehouse-sim.jpg",
        "featured": True,
        "blog_post": "warehouse-layout-optimization",
    }
]

SKILLS = {
    "Languages": ["Python", "SQL", "C++", "Bash"],
    "ML & AI": ["Scikit-learn", "TensorFlow", "LangChain", "Pandas", "NumPy", "Random Forest", "SVM", "Regression", "Deep Learning", "Target Marketing"],
    "Backend & Data": ["FastAPI", "PostgreSQL", "SQLAlchemy", "Alembic", "pgvector", "Kafka", "Docker"],
    "Cloud & Platforms": ["Azure", "Microsoft Fabric", "Snowflake", "Databricks", "Git", "Jira"],
}
