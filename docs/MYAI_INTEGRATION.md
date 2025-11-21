# myAI Integration Guide

This document outlines how to integrate myAI services and modules with the starter application.

## Overview

The myAI Starter Application is designed to seamlessly integrate with myAI services, providing a foundation for AI-powered applications.

## Configuration

### Environment Variables

Add the following to your `.env` file:

```bash
# myAI API Configuration
MYAI_API_KEY=your-api-key-here
MYAI_ENDPOINT=https://api.myai.example.com
MYAI_VERSION=v1
```

### Configuration Class

The configuration is already set up in `backend/app/core/config.py`:

```python
class Settings(BaseSettings):
    # myAI Integration
    MYAI_API_KEY: Optional[str] = None
    MYAI_ENDPOINT: Optional[str] = None
```

## Integration Points

### 1. API Authentication

Create a middleware or dependency for myAI authentication:

```python
# backend/app/core/myai_auth.py
from fastapi import Header, HTTPException
from app.core.config import settings

async def verify_myai_token(x_myai_token: str = Header(...)):
    """Verify myAI authentication token."""
    if not x_myai_token:
        raise HTTPException(status_code=401, detail="Missing myAI token")
    
    # Implement token verification logic
    # Call myAI service to validate token
    
    return x_myai_token
```

### 2. myAI Client

Create a client for myAI API calls:

```python
# backend/app/core/myai_client.py
import httpx
from app.core.config import settings

class MyAIClient:
    """Client for interacting with myAI services."""
    
    def __init__(self):
        self.base_url = settings.MYAI_ENDPOINT
        self.api_key = settings.MYAI_API_KEY
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    async def call_service(self, endpoint: str, data: dict):
        """Make a call to myAI service."""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/{endpoint}",
                json=data,
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
    
    async def health_check(self):
        """Check myAI service health."""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/health",
                headers=self.headers
            )
            return response.json()

# Singleton instance
myai_client = MyAIClient()
```

### 3. AI-Powered Endpoints

Example endpoint using myAI:

```python
# backend/app/api/ai.py
from fastapi import APIRouter, Depends
from app.core.myai_client import myai_client
from app.core.myai_auth import verify_myai_token
from pydantic import BaseModel

router = APIRouter()

class AIRequest(BaseModel):
    prompt: str
    parameters: dict = {}

class AIResponse(BaseModel):
    result: str
    confidence: float

@router.post("/ai/generate", response_model=AIResponse)
async def generate_ai_content(
    request: AIRequest,
    token: str = Depends(verify_myai_token)
):
    """Generate AI content using myAI service."""
    result = await myai_client.call_service(
        "generate",
        {
            "prompt": request.prompt,
            "parameters": request.parameters
        }
    )
    return AIResponse(**result)
```

### 4. Frontend Integration

Update the frontend to call AI endpoints:

```javascript
// frontend/public/app.js

async function callAI(prompt) {
  try {
    const response = await fetch('/api/v1/ai/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-MyAI-Token': 'your-token-here'
      },
      body: JSON.stringify({
        prompt: prompt,
        parameters: {}
      })
    });
    
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('AI call failed:', error);
    throw error;
  }
}
```

## myAI Modules

### Available Modules (Examples)

1. **Natural Language Processing**
   - Text generation
   - Sentiment analysis
   - Entity extraction
   - Language translation

2. **Computer Vision**
   - Image classification
   - Object detection
   - Image generation
   - OCR

3. **Predictive Analytics**
   - Forecasting
   - Anomaly detection
   - Recommendation systems

### Module Integration Pattern

```python
# backend/app/services/myai_service.py
from app.core.myai_client import myai_client

class MyAIService:
    """Service for myAI module integrations."""
    
    async def analyze_text(self, text: str):
        """Analyze text using NLP module."""
        return await myai_client.call_service(
            "nlp/analyze",
            {"text": text}
        )
    
    async def generate_image(self, prompt: str):
        """Generate image using computer vision module."""
        return await myai_client.call_service(
            "vision/generate",
            {"prompt": prompt}
        )
    
    async def get_recommendations(self, user_id: str, context: dict):
        """Get recommendations for user."""
        return await myai_client.call_service(
            "recommendations/get",
            {"user_id": user_id, "context": context}
        )

myai_service = MyAIService()
```

## Error Handling

### Retry Logic

```python
# backend/app/core/myai_retry.py
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10)
)
async def call_myai_with_retry(endpoint: str, data: dict):
    """Call myAI with automatic retry on failure."""
    return await myai_client.call_service(endpoint, data)
```

### Error Response Handling

```python
# backend/app/core/myai_errors.py
from fastapi import HTTPException

class MyAIError(Exception):
    """Base exception for myAI errors."""
    pass

class MyAIAuthError(MyAIError):
    """Authentication error with myAI."""
    pass

class MyAIRateLimitError(MyAIError):
    """Rate limit exceeded."""
    pass

def handle_myai_error(error):
    """Handle myAI errors and convert to HTTP exceptions."""
    if isinstance(error, MyAIAuthError):
        raise HTTPException(status_code=401, detail="myAI authentication failed")
    elif isinstance(error, MyAIRateLimitError):
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    else:
        raise HTTPException(status_code=500, detail="myAI service error")
```

## Monitoring

### Health Checks

Add myAI service check to readiness endpoint:

```python
# backend/app/api/health.py
from app.core.myai_client import myai_client

@router.get("/ready")
async def readiness_check():
    """Check if application and dependencies are ready."""
    checks = {
        "status": "ready",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "services": {}
    }
    
    # Check myAI service
    try:
        myai_status = await myai_client.health_check()
        checks["services"]["myai"] = "healthy"
    except Exception as e:
        checks["services"]["myai"] = f"unhealthy: {str(e)}"
        checks["status"] = "degraded"
    
    return checks
```

### Metrics

Track myAI usage:

```python
# backend/app/core/metrics.py
from collections import Counter
from datetime import datetime

class MyAIMetrics:
    """Track myAI usage metrics."""
    
    def __init__(self):
        self.calls = Counter()
        self.errors = Counter()
        self.response_times = []
    
    def record_call(self, endpoint: str, duration: float, success: bool):
        """Record a myAI call."""
        self.calls[endpoint] += 1
        self.response_times.append(duration)
        if not success:
            self.errors[endpoint] += 1
    
    def get_stats(self):
        """Get usage statistics."""
        return {
            "total_calls": sum(self.calls.values()),
            "total_errors": sum(self.errors.values()),
            "average_response_time": sum(self.response_times) / len(self.response_times) if self.response_times else 0,
            "calls_by_endpoint": dict(self.calls)
        }

myai_metrics = MyAIMetrics()
```

## Best Practices

1. **API Key Security**
   - Never commit API keys to version control
   - Use Azure Key Vault for production
   - Rotate keys regularly

2. **Rate Limiting**
   - Implement client-side rate limiting
   - Cache responses when appropriate
   - Use exponential backoff for retries

3. **Error Handling**
   - Always handle myAI service errors gracefully
   - Provide fallback behavior
   - Log errors for debugging

4. **Performance**
   - Use async/await for all myAI calls
   - Implement connection pooling
   - Cache frequently used results

5. **Testing**
   - Mock myAI responses in tests
   - Test error scenarios
   - Monitor integration in staging

## Example: Complete Integration

See the example below for a complete myAI integration:

```python
# backend/app/api/ai_example.py
from fastapi import APIRouter, Depends, HTTPException
from app.core.myai_client import myai_client
from app.core.myai_retry import call_myai_with_retry
from app.core.metrics import myai_metrics
from pydantic import BaseModel
import time

router = APIRouter()

class TextAnalysisRequest(BaseModel):
    text: str

class TextAnalysisResponse(BaseModel):
    sentiment: str
    entities: list
    keywords: list

@router.post("/analyze-text", response_model=TextAnalysisResponse)
async def analyze_text(request: TextAnalysisRequest):
    """Analyze text using myAI NLP module."""
    start_time = time.time()
    
    try:
        result = await call_myai_with_retry(
            "nlp/analyze",
            {"text": request.text}
        )
        
        duration = time.time() - start_time
        myai_metrics.record_call("nlp/analyze", duration, True)
        
        return TextAnalysisResponse(**result)
        
    except Exception as e:
        duration = time.time() - start_time
        myai_metrics.record_call("nlp/analyze", duration, False)
        raise HTTPException(
            status_code=500,
            detail=f"Failed to analyze text: {str(e)}"
        )
```

## Next Steps

1. Obtain myAI API credentials
2. Configure environment variables
3. Implement the client and authentication
4. Create API endpoints for your use cases
5. Add monitoring and error handling
6. Test integration thoroughly
7. Deploy to production

## Support

For myAI-specific questions:
- Contact myAI support team
- Review myAI documentation
- Check myAI community forums

For integration issues:
- Open an issue in this repository
- Contact the development team
