# Deployment Guide

This guide covers various deployment options for the myAI Starter Application.

## Table of Contents

1. [Local Development](#local-development)
2. [Docker Deployment](#docker-deployment)
3. [Azure Deployment](#azure-deployment)
4. [Heroku Deployment](#heroku-deployment)
5. [Production Checklist](#production-checklist)

## Local Development

### Prerequisites
- Python 3.10+
- pip

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
   cd YOUR-REPO-NAME
   ```

2. Set up environment:
   ```bash
   cp .env.template .env
   # Edit .env with your configuration
   ```

3. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python -m app.main
   ```

5. Access at http://localhost:8000

## Docker Deployment

### Using Docker Compose (Recommended)

1. Build and run:
   ```bash
   docker-compose up -d
   ```

2. View logs:
   ```bash
   docker-compose logs -f
   ```

3. Stop:
   ```bash
   docker-compose down
   ```

### Using Docker Directly

1. Build the image:
   ```bash
   docker build -t myai-starter .
   ```

2. Run the container:
   ```bash
   docker run -d \
     --name myai-starter \
     -p 8000:8000 \
     -e DEBUG=False \
     myai-starter
   ```

3. View logs:
   ```bash
   docker logs -f myai-starter
   ```

## Azure Deployment

### Option 1: Azure App Service (Recommended)

#### Using Azure Portal

1. **Create App Service**
   - Navigate to Azure Portal
   - Create Resource → Web App
   - Choose Python 3.12 runtime
   - Select appropriate pricing tier

2. **Configure Settings**
   - Go to Configuration
   - Add application settings from `.env.template`
   - Save changes

3. **Deploy Code**
   
   Using Azure CLI:
   ```bash
   az login
   az webapp up \
     --name myai-starter-app \
     --resource-group myai-starter-rg \
     --runtime "PYTHON:3.12"
   ```

   Or using GitHub Actions (see `.github/workflows/` for examples)

#### Using Azure CLI

Complete setup:

```bash
# Login
az login

# Create resource group
az group create \
  --name myai-starter-rg \
  --location eastus

# Create App Service plan
az appservice plan create \
  --name myai-starter-plan \
  --resource-group myai-starter-rg \
  --sku B1 \
  --is-linux

# Create web app
az webapp create \
  --name myai-starter-app \
  --resource-group myai-starter-rg \
  --plan myai-starter-plan \
  --runtime "PYTHON:3.12"

# Configure environment variables
az webapp config appsettings set \
  --name myai-starter-app \
  --resource-group myai-starter-rg \
  --settings \
    DEBUG=False \
    APP_NAME="myAI Starter API" \
    PORT=8000

# Deploy code
cd /path/to/project
az webapp up \
  --name myai-starter-app \
  --resource-group myai-starter-rg
```

### Option 2: Azure Container Instances

```bash
# Build and push to Azure Container Registry
az acr create \
  --name myaistarter \
  --resource-group myai-starter-rg \
  --sku Basic

az acr build \
  --registry myaistarter \
  --image myai-starter:latest .

# Deploy to ACI
az container create \
  --name myai-starter-container \
  --resource-group myai-starter-rg \
  --image myaistarter.azurecr.io/myai-starter:latest \
  --cpu 1 --memory 1 \
  --registry-username <username> \
  --registry-password <password> \
  --dns-name-label myai-starter \
  --ports 8000
```

### Option 3: Azure Kubernetes Service (AKS)

For production scale deployments:

```bash
# Create AKS cluster
az aks create \
  --resource-group myai-starter-rg \
  --name myai-starter-aks \
  --node-count 2 \
  --enable-managed-identity

# Get credentials
az aks get-credentials \
  --resource-group myai-starter-rg \
  --name myai-starter-aks

# Deploy using kubectl
kubectl apply -f k8s/deployment.yaml
```

## Heroku Deployment

1. **Create Heroku app**:
   ```bash
   heroku create myai-starter-app
   ```

2. **Create `Procfile`** in project root:
   ```
   web: cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```

3. **Create `runtime.txt`**:
   ```
   python-3.12.0
   ```

4. **Set environment variables**:
   ```bash
   heroku config:set DEBUG=False
   heroku config:set APP_NAME="myAI Starter API"
   ```

5. **Deploy**:
   ```bash
   git push heroku main
   ```

6. **Open app**:
   ```bash
   heroku open
   ```

## AWS Deployment

### Using Elastic Beanstalk

1. **Install EB CLI**:
   ```bash
   pip install awsebcli
   ```

2. **Initialize**:
   ```bash
   eb init -p python-3.12 myai-starter
   ```

3. **Create environment**:
   ```bash
   eb create myai-starter-env
   ```

4. **Deploy**:
   ```bash
   eb deploy
   ```

5. **Open**:
   ```bash
   eb open
   ```

## Google Cloud Platform

### Using Cloud Run

1. **Build and push**:
   ```bash
   gcloud builds submit --tag gcr.io/PROJECT_ID/myai-starter
   ```

2. **Deploy**:
   ```bash
   gcloud run deploy myai-starter \
     --image gcr.io/PROJECT_ID/myai-starter \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```

## Production Checklist

### Security

- [ ] Change all default passwords and secrets
- [ ] Use environment variables for sensitive data
- [ ] Enable HTTPS/SSL
- [ ] Configure CORS properly
- [ ] Implement rate limiting
- [ ] Enable security headers
- [ ] Use Azure Key Vault for secrets
- [ ] Implement authentication/authorization
- [ ] Keep dependencies updated
- [ ] Enable audit logging

### Performance

- [ ] Enable caching where appropriate
- [ ] Configure CDN for static assets
- [ ] Optimize database queries
- [ ] Enable compression
- [ ] Set up connection pooling
- [ ] Configure auto-scaling
- [ ] Monitor resource usage
- [ ] Set up health checks

### Monitoring

- [ ] Configure Application Insights
- [ ] Set up error tracking
- [ ] Configure alerts for critical metrics
- [ ] Enable request/response logging
- [ ] Monitor API response times
- [ ] Track error rates
- [ ] Monitor resource utilization
- [ ] Set up uptime monitoring

### Database

- [ ] Configure backups
- [ ] Set up replication (if needed)
- [ ] Enable connection pooling
- [ ] Configure proper indexes
- [ ] Set up migrations
- [ ] Document schema

### Documentation

- [ ] Update API documentation
- [ ] Document environment variables
- [ ] Create runbooks for common issues
- [ ] Document deployment process
- [ ] Update architecture diagrams

### Testing

- [ ] Run full test suite
- [ ] Perform load testing
- [ ] Test error scenarios
- [ ] Verify integrations
- [ ] Test rollback procedures

### Compliance

- [ ] Review data privacy requirements
- [ ] Implement data retention policies
- [ ] Configure audit logging
- [ ] Document compliance measures
- [ ] Perform security assessment

## Environment Variables

Required for production:

```bash
# Application
DEBUG=False
APP_NAME="myAI Starter API"
HOST=0.0.0.0
PORT=8000

# CORS (update with your domains)
CORS_ORIGINS=["https://yourdomain.com"]

# Azure (if using Azure services)
AZURE_TENANT_ID=your-tenant-id
AZURE_CLIENT_ID=your-client-id
AZURE_CLIENT_SECRET=your-client-secret

# Database (if using)
DATABASE_URL=your-database-url

# myAI
MYAI_API_KEY=your-api-key
MYAI_ENDPOINT=https://api.myai.example.com
```

## Scaling Strategies

### Horizontal Scaling

- Use load balancer
- Multiple app instances
- Session storage in Redis/database
- Stateless application design

### Vertical Scaling

- Increase CPU/memory resources
- Optimize code performance
- Use async operations
- Implement caching

### Database Scaling

- Read replicas
- Connection pooling
- Query optimization
- Caching layer

## Troubleshooting

### Application won't start

1. Check logs: `docker logs <container>` or platform-specific logs
2. Verify environment variables
3. Check port availability
4. Verify dependencies installed

### Performance issues

1. Check Application Insights metrics
2. Review database query performance
3. Check for memory leaks
4. Monitor CPU usage
5. Review caching configuration

### Connection issues

1. Verify network configuration
2. Check firewall rules
3. Verify DNS settings
4. Check SSL/TLS configuration

## Rollback Procedures

### Azure App Service

```bash
# Swap slots
az webapp deployment slot swap \
  --name myai-starter-app \
  --resource-group myai-starter-rg \
  --slot staging \
  --target-slot production
```

### Docker

```bash
# Revert to previous image
docker run -d \
  --name myai-starter \
  -p 8000:8000 \
  myai-starter:previous-tag
```

### General

1. Identify the working version
2. Deploy previous version
3. Verify functionality
4. Update documentation
5. Investigate root cause

## Additional Resources

- [Azure App Service Docs](https://docs.microsoft.com/azure/app-service/)
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
