# AI Job Search Assistant

An AI-assisted job search application with a FastAPI backend, agent workflows, and APIs for managing job-search activities.

## Features

- Agent-based career and job-search workflows
- Resume and application endpoints
- Job and user management APIs
- Authentication and chat endpoints
- PostgreSQL integration
- Logging and observability utilities
- Backend endpoint tests

## Tech Stack

Python, FastAPI, SQLAlchemy, PostgreSQL, Pydantic, LangChain integrations, and Docker Compose.

## Project Structure

```text
ai-job-search-assistant/
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── api/
│   │   ├── database/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── security/
│   │   └── main.py
│   ├── tests/
│   └── requirements.txt
├── docs/
├── frontend/
├── docker-compose.yml
└── README.md
```

## Setup

```bash
git clone https://github.com/gopalrajane/ai-job-search-assistant.git
cd ai-job-search-assistant/backend
python -m venv .venv
```

Activate the environment, then install dependencies:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Create a local environment file from `.env.example` and configure the required database and API settings before running the application. Use Docker Compose when running the full service stack.

## Author

[Gopal Rajane](https://github.com/gopalrajane) · [LinkedIn](https://www.linkedin.com/in/gopal-rajane/)
