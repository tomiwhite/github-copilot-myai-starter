# Azure Integration

This directory contains configuration and documentation for Azure services integration.

## Planned Azure Services

### 1. Azure App Service
Deploy the web application to Azure App Service for production hosting.

**Configuration needed:**
- App Service Plan
- Web App resource
- Environment variables configuration
- Deployment slots (staging/production)

**GitHub Actions Deployment:**
See `.github/workflows/azure-deploy.yml` (to be created)

### 2. Azure Cosmos DB
NoSQL database for scalable data storage.

**Configuration:**
```python
# In backend/app/core/config.py
COSMOS_DB_ENDPOINT: Optional[str] = None
COSMOS_DB_KEY: Optional[str] = None
COSMOS_DB_DATABASE: str = "myai_starter"
```

**Implementation:**
- Add `azure-cosmos` package to requirements.txt
- Create repository layer for Cosmos DB operations
- Implement connection management

### 3. Azure Storage
Blob storage for files and static assets.

**Configuration:**
```python
# In backend/app/core/config.py
AZURE_STORAGE_CONNECTION_STRING: Optional[str] = None
AZURE_STORAGE_CONTAINER: str = "uploads"
```

**Use cases:**
- User uploads
- Generated reports
- Static assets (images, documents)

### 4. Azure Key Vault
Secure secret management.

**Configuration:**
```python
# In backend/app/core/config.py
AZURE_KEY_VAULT_URL: Optional[str] = None
```

**Secrets to store:**
- Database connection strings
- API keys
- Service credentials
- Certificates

### 5. Application Insights
Monitoring and analytics.

**Configuration:**
```python
# In backend/app/core/config.py
APPINSIGHTS_INSTRUMENTATION_KEY: Optional[str] = None
```

**Features:**
- Performance monitoring
- Error tracking
- Usage analytics
- Custom events and metrics

### 6. Azure AD / Entra ID
Authentication and authorization.

**Configuration:**
```python
# In backend/app/core/config.py
AZURE_AD_TENANT_ID: Optional[str] = None
AZURE_AD_CLIENT_ID: Optional[str] = None
AZURE_AD_CLIENT_SECRET: Optional[str] = None
```

**Implementation:**
- OAuth2 flow
- JWT token validation
- Role-based access control

### 7. Azure Functions
Serverless compute for background tasks.

**Use cases:**
- Scheduled jobs
- Event-driven processing
- Data transformations
- Integration webhooks

### 8. Azure Service Bus
Message queue for async processing.

**Configuration:**
```python
# In backend/app/core/config.py
AZURE_SERVICE_BUS_CONNECTION_STRING: Optional[str] = None
```

**Use cases:**
- Background job queue
- Event streaming
- Microservices communication

## Setup Instructions

### Prerequisites

1. Azure subscription
2. Azure CLI installed
3. Appropriate permissions

### Initial Setup

```bash
# Login to Azure
az login

# Create resource group
az group create --name myai-starter-rg --location eastus

# Create App Service Plan
az appservice plan create \
  --name myai-starter-plan \
  --resource-group myai-starter-rg \
  --sku B1 \
  --is-linux

# Create Web App
az webapp create \
  --name myai-starter-app \
  --resource-group myai-starter-rg \
  --plan myai-starter-plan \
  --runtime "PYTHON:3.12"
```

### Environment Variables

Configure in Azure Portal or via CLI:

```bash
az webapp config appsettings set \
  --name myai-starter-app \
  --resource-group myai-starter-rg \
  --settings \
    DEBUG=False \
    APP_NAME="myAI Starter API" \
    CORS_ORIGINS='["https://myai-starter-app.azurewebsites.net"]'
```

### Deploy Application

```bash
# Build and deploy
az webapp up \
  --name myai-starter-app \
  --resource-group myai-starter-rg \
  --runtime "PYTHON:3.12"
```

## Cost Optimization

- Use Free/Basic tier for development
- Scale up for production based on load
- Use Azure Cost Management to monitor spending
- Leverage reserved instances for predictable workloads

## Security Best Practices

1. **Never commit secrets** - Use Key Vault or environment variables
2. **Enable HTTPS only** - Enforce SSL/TLS
3. **Use managed identities** - Avoid storing credentials
4. **Implement network security** - Use VNets and NSGs
5. **Enable monitoring** - Use Application Insights and Azure Monitor
6. **Regular updates** - Keep dependencies and platform updated

## Monitoring and Diagnostics

### Application Insights Queries

```kusto
// Request success rate
requests
| summarize SuccessRate = 100.0 * countif(success == true) / count() by bin(timestamp, 5m)

// Failed requests
requests
| where success == false
| project timestamp, name, resultCode, duration

// Performance
requests
| summarize avg(duration), percentile(duration, 95) by name
```

### Alerts Configuration

Set up alerts for:
- High error rate (> 5%)
- Slow response time (> 2s)
- High CPU usage (> 80%)
- High memory usage (> 85%)

## Scaling Strategy

### Horizontal Scaling
```bash
az appservice plan update \
  --name myai-starter-plan \
  --resource-group myai-starter-rg \
  --number-of-workers 3
```

### Auto-scaling Rules
- Scale out when CPU > 70%
- Scale in when CPU < 30%
- Min instances: 1
- Max instances: 10

## Backup and Recovery

1. **Database backups** - Automated daily backups
2. **Configuration backups** - Version control
3. **Disaster recovery plan** - Multi-region deployment
4. **Testing** - Regular DR drills

## Additional Resources

- [Azure App Service Documentation](https://docs.microsoft.com/en-us/azure/app-service/)
- [Azure Cosmos DB Documentation](https://docs.microsoft.com/en-us/azure/cosmos-db/)
- [Application Insights Documentation](https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)
- [Azure Best Practices](https://docs.microsoft.com/en-us/azure/architecture/best-practices/)
