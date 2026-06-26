# Production Deployment on Google Cloud

## Prerequisites

```bash
# Install Google Cloud SDK
curl https://sdk.cloud.google.com | bash

# Initialize
gcloud init
gcloud config set project YOUR_PROJECT_ID

# Enable required APIs
gcloud services enable \
  cloudbuild.googleapis.com \
  run.googleapis.com \
  compute.googleapis.com \
  cloudsql.googleapis.com \
  redis.googleapis.com
```

## Database Setup (Cloud SQL)

```bash
# Create PostgreSQL instance
gcloud sql instances create job-assistant-db \
  --database-version=POSTGRES_15 \
  --region=us-central1 \
  --tier=db-custom-2-7680

# Create database
gcloud sql databases create job_assistant --instance=job-assistant-db

# Create user
gcloud sql users create jobassistant --instance=job-assistant-db --password=YOUR_PASSWORD
```

## Redis Cache Setup (Memorystore)

```bash
# Create Redis instance
gcloud redis instances create job-assistant-cache \
  --size=2 \
  --region=us-central1 \
  --redis-version=7.0
```

## Deployment

```bash
# Set environment variables
export GCP_PROJECT_ID=your-project-id
export DATABASE_URL=postgresql://user:pass@ip/db
export REDIS_URL=redis://ip:6379
export SECRET_KEY=your-secret-key
export OPENAI_API_KEY=your-api-key

# Run deployment script
bash scripts/deploy-gcp.sh
```

## Monitoring

```bash
# View logs
gcloud run logs read ai-job-assistant-backend --region us-central1 --limit 50

# Set up monitoring
gcloud monitoring dashboards create --config-from-file=monitoring-dashboard.yaml
```

## Auto-scaling Configuration

```bash
gcloud run services update-traffic ai-job-assistant-backend \
  --region=us-central1 \
  --max-instances=100 \
  --min-instances=1
```

## Domain Setup

```bash
# Map custom domain
gcloud run domain-mappings create \
  --service=ai-job-assistant-frontend \
  --domain=yourdomain.com \
  --region=us-central1
```
