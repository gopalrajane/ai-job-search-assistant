# AI Job Search Assistant

> **Production-ready AI Job Search Assistant with Multi-Agent Architecture**
>
> An intelligent platform combining Google's ADK 2.0 multi-agent architecture with specialized agents for job search, resume analysis, ATS scoring, interview prep, and career guidance.

## 🎯 Features

### Core Capabilities
- **Multi-Agent Orchestration**: Central Orchestrator Agent coordinating 7 specialized agents
- **Resume Analysis**: PDF/DOCX parsing with automatic skill/education/experience extraction
- **Real Job Integration**: Live job search with provider abstraction and mock fallback
- **ATS Scoring**: Job match scoring (0-100%) with skill gap analysis
- **Cover Letter Generation**: AI-powered with human-in-the-loop approval
- **Interview Preparation**: Real-time interview coaching and feedback
- **Career Roadmap**: Personalized career progression planning
- **Salary Insights**: Market-based salary analysis and negotiation tips

### Security & Compliance
- Prompt injection detection
- PII redaction and data privacy
- Scam detection for suspicious jobs
- Comprehensive audit logging
- Configurable security policies
- Role-based access control (RBAC)

### Technical Stack
- **Backend**: FastAPI with async support, validation, authentication
- **Frontend**: React + TypeScript with modern dashboard
- **Database**: PostgreSQL for persistent storage
- **AI/ML**: LangChain, Claude AI, OpenAI integration
- **Deployment**: Docker, Docker Compose, Google Cloud (Cloud Run)
- **CI/CD**: GitHub Actions
- **Observability**: OpenTelemetry, structured logging
- **Testing**: Pytest (unit, integration, e2e)

## 📋 Project Structure

```
ai-job-search-assistant/
├── backend/                          # FastAPI Application
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                  # FastAPI app entry
│   │   ├── config.py                # Configuration management
│   │   ├── dependencies.py          # Dependency injection
│   │   ├── agents/                  # Multi-agent orchestration
│   │   │   ├── __init__.py
│   │   │   ├── orchestrator.py      # Main orchestrator agent
│   │   │   ├── job_search.py        # Job search agent
│   │   │   ├── resume_analysis.py   # Resume analysis agent
│   │   │   ├── ats_scoring.py       # ATS scoring agent
│   │   │   ├── cover_letter.py      # Cover letter generation
│   │   │   ├── interview_prep.py    # Interview preparation
│   │   │   ├── career_roadmap.py    # Career planning
│   │   │   └── salary_insights.py   # Salary analysis
│   │   ├── mcp/                     # MCP Tools
│   │   │   ├── __init__.py
│   │   │   ├── job_search_tool.py
│   │   │   ├── resume_parser.py
│   │   │   ├── company_insights.py
│   │   │   ├── ats_scorer.py
│   │   │   ├── interview_optimizer.py
│   │   │   ├── salary_tool.py
│   │   │   ├── learning_resources.py
│   │   │   └── application_tracker.py
│   │   ├── security/                # Security modules
│   │   │   ├── __init__.py
│   │   │   ├── prompt_injection.py  # Prompt injection detection
│   │   │   ├── pii_redaction.py     # PII redaction
│   │   │   ├── scam_detection.py    # Scam detection
│   │   │   ├── audit_logger.py      # Audit logging
│   │   │   └── policies.py          # Security policies
│   │   ├── models/                  # Database models
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── resume.py
│   │   │   ├── job.py
│   │   │   ├── application.py
│   │   │   ├── conversation.py
│   │   │   └── preferences.py
│   │   ├── schemas/                 # Pydantic schemas
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── resume.py
│   │   │   ├── job.py
│   │   │   ├── application.py
│   │   │   └── conversation.py
│   │   ├── api/                     # API routes
│   │   │   ├── __init__.py
│   │   │   ├── auth.py              # Authentication
│   │   │   ├── users.py             # User management
│   │   │   ├── resumes.py           # Resume operations
│   │   │   ├── jobs.py              # Job search & matching
│   │   │   ├── applications.py      # Application tracking
│   │   │   ├── agents.py            # Agent interactions
│   │   │   ├── chat.py              # Chat/conversation
│   │   │   └── health.py            # Health checks
│   │   ├── database/                # Database setup
│   │   │   ├── __init__.py
│   │   │   ├── session.py           # SQLAlchemy session
│   │   │   └── migrations/          # Alembic migrations
│   │   ├── utils/                   # Utility functions
│   │   │   ├── __init__.py
│   │   │   ├── logger.py            # Logging setup
│   │   │   ├── validators.py        # Validators
│   │   │   └── helpers.py           # Helper functions
│   │   └── services/                # Business logic services
│   │       ├── __init__.py
│   │       ├── resume_service.py
│   │       ├── job_service.py
│   │       └── chat_service.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── conftest.py              # Pytest fixtures
│   │   ├── test_agents/
│   │   ├── test_api/
│   │   ├── test_security/
│   │   └── test_services/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
│
├── frontend/                         # React + TypeScript
│   ├── src/
│   │   ├── components/
│   │   │   ├── Dashboard.tsx
│   │   │   ├── ChatInterface.tsx
│   │   │   ├── ResumeUpload.tsx
│   │   │   ├── JobCards.tsx
│   │   │   ├── ApplicationTracker.tsx
│   │   │   ├── SalaryInsights.tsx
│   │   │   ├── InterviewPrep.tsx
│   │   │   └── CareerRoadmap.tsx
│   │   ├── pages/
│   │   │   ├── Home.tsx
│   │   │   ├── Dashboard.tsx
│   │   │   ├── Jobs.tsx
│   │   │   ├── Resume.tsx
│   │   │   ├── Applications.tsx
│   │   │   ├── Analytics.tsx
│   │   │   └── Settings.tsx
│   │   ├── hooks/
│   │   │   ├── useAuth.ts
│   │   │   ├── useChat.ts
│   │   │   ├── useJobs.ts
│   │   │   └── useResume.ts
│   │   ├── services/
│   │   │   ├── api.ts
│   │   │   ├── auth.ts
│   │   │   └── storage.ts
│   │   ├── types/
│   │   │   ├── index.ts
│   │   │   ├── user.ts
│   │   │   ├── job.ts
│   │   │   └── resume.ts
│   │   ├── styles/
│   │   │   ├── globals.css
│   │   │   ├── themes.css
│   │   │   └── responsive.css
│   │   ├── utils/
│   │   │   ├── formatters.ts
│   │   │   └── validators.ts
│   │   ├── App.tsx
│   │   └── index.tsx
│   ├── public/
│   ├── package.json
│   ├── tsconfig.json
│   ├── Dockerfile
│   └── .env.example
│
├── docker-compose.yml               # Local development
├── docker-compose.prod.yml          # Production setup
├── .github/
│   └── workflows/
│       ├── ci.yml                   # CI pipeline
│       ├── deploy.yml               # Deployment workflow
│       └── tests.yml                # Test pipeline
├── kubernetes/                      # K8s configs (optional)
│   ├── backend-deployment.yaml
│   ├── frontend-deployment.yaml
│   └── postgres-statefulset.yaml
├── docs/
│   ├── API.md
│   ├── ARCHITECTURE.md
│   ├── DEPLOYMENT.md
│   ├── CONTRIBUTING.md
│   └── USER_GUIDE.md
├── scripts/
│   ├── setup.sh
│   ├── deploy.sh
│   └── migrate.sh
└── .env.example
```

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.11+
- Node.js 18+
- PostgreSQL 15+

### Local Development

```bash
# Clone the repository
git clone https://github.com/gopalrajane/ai-job-search-assistant.git
cd ai-job-search-assistant

# Copy environment variables
cp .env.example .env

# Start with Docker Compose
docker-compose up -d

# Backend will be at: http://localhost:8000
# Frontend will be at: http://localhost:3000
# API Docs at: http://localhost:8000/docs
```

### Manual Setup

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## 🔧 Configuration

Create `.env` file with:

```env
# Backend
DATABASE_URL=postgresql://user:password@localhost:5432/job_assistant
SECRET_KEY=your-secret-key-here
ALLOWED_ORIGINS=http://localhost:3000

# AI Models
OPENAI_API_KEY=sk-...
CLAUDE_API_KEY=sk-...

# Job APIs
LINKEDIN_API_KEY=
INDEED_API_KEY=

# Security
ENCRYPTION_KEY=
AUDIT_LOG_ENABLED=true

# Frontend
REACT_APP_API_URL=http://localhost:8000/api
```

## 📊 Database Schema

- **users**: User profiles and authentication
- **resumes**: Uploaded resumes with extracted data
- **jobs**: Discovered jobs and bookmarks
- **applications**: Application history and tracking
- **conversations**: Chat history and agent interactions
- **preferences**: User preferences and settings
- **audit_logs**: Security audit trail

## 🧪 Testing

```bash
# Unit tests
pytest tests/unit

# Integration tests
pytest tests/integration

# E2E tests
pytest tests/e2e

# Coverage report
pytest --cov=app tests/
```

## 🐳 Docker Deployment

```bash
# Build images
docker-compose build

# Production deployment
docker-compose -f docker-compose.prod.yml up -d
```

## ☁️ Google Cloud Deployment

```bash
# Deploy backend to Cloud Run
bash scripts/deploy.sh backend

# Deploy frontend to Cloud Run
bash scripts/deploy.sh frontend
```

## 📈 Monitoring & Observability

- OpenTelemetry integration for distributed tracing
- Structured JSON logging
- Prometheus metrics export
- Google Cloud Logging integration

## 🔐 Security Features

- ✅ Prompt injection detection
- ✅ PII redaction (SSN, email, phone)
- ✅ Scam job detection
- ✅ Comprehensive audit logging
- ✅ Role-based access control (RBAC)
- ✅ Rate limiting and DDoS protection
- ✅ CORS and CSRF protection

## 📚 Documentation

- [Architecture Guide](./docs/ARCHITECTURE.md)
- [API Reference](./docs/API.md)
- [Deployment Guide](./docs/DEPLOYMENT.md)
- [Contributing Guidelines](./docs/CONTRIBUTING.md)
- [User Guide](./docs/USER_GUIDE.md)

## 🤝 Contributing

See [CONTRIBUTING.md](./docs/CONTRIBUTING.md) for guidelines.

## 📝 License

MIT License - see LICENSE file

## 👨‍💻 Author

Built by Gopal Rajane

---

**Questions or Issues?** Open an issue on GitHub!
