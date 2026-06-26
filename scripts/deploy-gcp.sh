#!/bin/bash

# Production deployment script for Google Cloud

set -e

PROJECT_ID=${GCP_PROJECT_ID:-"your-project-id"}
REGION=${GCP_REGION:-"us-central1"}
IMAGE_NAME="gcr.io/${PROJECT_ID}/ai-job-assistant"

echo "Deploying AI Job Search Assistant to Google Cloud..."

# Build and push backend
echo "Building backend image..."
cd backend
gcloud builds submit --tag ${IMAGE_NAME}-backend:latest --project ${PROJECT_ID}

echo "Deploying backend to Cloud Run..."
gcloud run deploy ai-job-assistant-backend \
  --image ${IMAGE_NAME}-backend:latest \
  --platform managed \
  --region ${REGION} \
  --project ${PROJECT_ID} \
  --memory 2Gi \
  --cpu 2 \
  --timeout 3600 \
  --set-env-vars "DATABASE_URL=${DATABASE_URL},REDIS_URL=${REDIS_URL},SECRET_KEY=${SECRET_KEY},OPENAI_API_KEY=${OPENAI_API_KEY}" \
  --allow-unauthenticated

# Build and push frontend
echo "Building frontend image..."
cd ../frontend
npm run build
gcloud builds submit --tag ${IMAGE_NAME}-frontend:latest --project ${PROJECT_ID}

echo "Deploying frontend to Cloud Run..."
gcloud run deploy ai-job-assistant-frontend \
  --image ${IMAGE_NAME}-frontend:latest \
  --platform managed \
  --region ${REGION} \
  --project ${PROJECT_ID} \
  --memory 1Gi \
  --cpu 1 \
  --allow-unauthenticated

echo "Deployment complete!"
echo "Backend: https://ai-job-assistant-backend-${REGION}.a.run.app"
echo "Frontend: https://ai-job-assistant-frontend-${REGION}.a.run.app"
